import logging
import time

from src.common import MediaController
from src.main import Dispatcher, listen_once
from src.voice_input import VoiceInput


class RecordingController(MediaController):
    """A deterministic backend used to measure application overhead only."""

    def __init__(self) -> None:
        self.calls: list[str] = []

    def volume_up(self) -> None:
        self.calls.append("volume_up")

    def volume_down(self) -> None:
        self.calls.append("volume_down")

    def play(self) -> None:
        self.calls.append("play")

    def pause(self) -> None:
        self.calls.append("pause")

    def resume(self) -> None:
        self.calls.append("resume")

    def next_track(self) -> None:
        self.calls.append("next_track")

    def previous_track(self) -> None:
        self.calls.append("previous_track")


class DeterministicVoice:
    def capture(self) -> str:
        return "volume up"


class FakeMicrophone:
    def __enter__(self) -> "FakeMicrophone":
        return self

    def __exit__(self, exc_type, exc_value, traceback) -> None:
        return None


class FakeRecognizer:
    def listen(self, source, timeout, phrase_time_limit):
        return object()

    def recognize_google(self, audio) -> str:
        return "  Volume Up  "


def test_command_processing_meets_two_second_target_over_100_runs():
    """TC-11: measure the deterministic capture-to-dispatch path."""
    controller = RecordingController()
    dispatcher = Dispatcher(controller, volume_steps=1)
    durations = []

    for _ in range(100):
        started = time.perf_counter()
        listen_once(DeterministicVoice(), dispatcher, output=lambda message: None)
        durations.append(time.perf_counter() - started)

    assert controller.calls == ["volume_up"] * 100
    assert sum(duration < 2 for duration in durations) >= 95


def test_voice_input_keeps_audio_and_transcript_in_memory(tmp_path, monkeypatch, caplog):
    """TC-15: normal recognition neither writes files nor emits transcript logs."""
    monkeypatch.chdir(tmp_path)
    voice_input = VoiceInput(
        recognizer=FakeRecognizer(),
        microphone_factory=FakeMicrophone,
        listen_timeout=1.0,
        phrase_time_limit=1.0,
    )

    with caplog.at_level(logging.DEBUG):
        assert voice_input.capture() == "Volume Up"

    assert list(tmp_path.iterdir()) == []
    assert caplog.records == []
