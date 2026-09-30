# Voice Assistant for Multimedia Controls

## 1. Project Overview

The aim of this project is to build a simple voice-controlled multimedia assistant.

The user will be able to control basic media functions using voice commands.


## 2. Main Features

The system should support the following commands:

- Volume Up
- Volume Down
- Play
- Pause
- Resume
- Next
- Previous

## 3. Functional Requirements

### FR1 - Voice Input
The system should accept voice commands from the user through a microphone.

### FR2 - Volume Control
The system should increase or decrease the volume when the user says:
- "Volume Up"
- "Volume Down"

### FR3 - Playback Control
The system should control media playback when the user says:
- "Play"
- "Pause"
- "Resume"

### FR4 - Track Control
The system should change the current media track when the user says:
- "Next"
- "Previous"

### FR5 - Invalid Command
If the spoken command is not supported, the system should ignore it or display a simple message.

## 4. Non-Functional Requirements

- The system should be simple to use.
- The response to a valid command should be reasonably fast.
- The code should be modular and easy to understand.
- The system should handle unsupported commands without crashing.

## 5. Initial Technology

- Python
- Raspberry Pi / ESP-based hardware {I think ESP is better as we already have it}
- Microphone {We can use laptop's microphone also like playing videos in laptop directly}
- Media control libraries/tools


## 6. Team Members

- Member 1: Rohan
- Member 2: Ujwal
- Member 3: Venkatesh
- Member 4: Yashas

## 7. Work Division

The course guidelines require that **each member completes one full functional feature** (UI, testing and DB work don't count as features), and that every member has their own git commits. So the split below is by feature, with each feature in its own module to keep PRs independent. Work is sized in rough effort points (1 = small, 3 = large) so the load is even.

> Names below are a proposed assignment; swap them if the team prefers.

### 7.1 Feature ownership

| Member | Feature | Requirements | Module | Effort |
|---|---|---|---|---|
| Rohan | Voice Input: microphone capture, speech-to-text, silence/timeout handling | FR1 | `src/voice_input/` | 3 |
| Ujwal | Command Recognition: text to command mapping, invalid-command handling, main dispatcher loop. Volume Control (up / down, limits) | FR5, FR2 | `src/command_parser/`, `src/main.py`, `src/volume/` | 2 + 1 |
| Venkatesh | Playback Control: play / pause / resume with playback state | FR3 | `src/playback/` | 2 (+ CI/CD below) |
| Yashas | Track Control: next / previous. Media Backend: OS-level media control adapter used by volume, playback and track | FR4 | `src/track/`, `src/media_backend/` | 1 + 2 |

Totals are roughly 3 / 3 / 2+CI / 3 points. Venkatesh's lighter feature is offset by the CI/CD setup below.

### 7.2 Quality / process ownership

| Member | Concern |
|---|---|
| Rohan | Response time of a valid command (target: reasonably fast, e.g. under 2 s) |
| Ujwal | Security validation and static analysis (SonarQube or similar) |
| Venkatesh | CI/CD pipeline (Jenkins), unit test and code coverage reports |
| Yashas | Jira board and sprint tracking |

Everyone writes their own module's tests (pytest) and fills in their own rows of the requirements traceability matrix.

### 7.3 Shared pieces

- `src/common/` holds the shared interface (e.g. a `Command` enum and a `MediaController` interface). All four agree on it in the first sprint and it is merged first, so everyone codes against the same contract.
- `src/media_backend/` implements that interface; volume, playback and track modules call it rather than touching the OS directly, so the laptop-vs-ESP decision only changes this one module and `voice_input`.

### 7.4 Working agreement

- One branch per feature (`feature/voice-input`, `feature/command-parser`, `feature/volume`, `feature/playback`, `feature/track`, `feature/media-backend`); no direct pushes to `main`.
- Every PR needs at least one review from another member before merge.
- Every PR links to its Jira user story.


## 8. Current Scope

For the first version, the project will focus only on basic voice-based multimedia control.

Additional features can be added later after the basic system is working.