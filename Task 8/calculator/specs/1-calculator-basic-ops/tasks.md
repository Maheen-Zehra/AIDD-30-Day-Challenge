# Tasks: Simple Calculator with Basic Operations

**Input**: Design documents from `/specs/1-calculator-basic-ops/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [x] T001 Create project structure `src/calculator`, `tests/unit`, `tests/integration`
- [x] T002 Create `__init__.py` files in `src/calculator`, `tests/unit`, `tests/integration`

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T003 Install `pytest` and configure basic `pytest.ini`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Perform Basic Arithmetic (Priority: P1) 🎯 MVP

**Goal**: As a user, I want to input a mathematical expression with basic operations (addition, subtraction, multiplication, division) and receive the correct numerical result.

**Independent Test**: Can be fully tested by providing various valid expressions (e.g., "2+2", "10-5", "3*4", "10/2") and verifying the output matches the expected mathematical result.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T004 [US1] Create unit tests for parsing valid basic arithmetic expressions in `tests/unit/test_parser.py`
- [x] T005 [US1] Create unit tests for evaluating valid basic arithmetic operations in `tests/unit/test_evaluator.py`
- [x] T006 [US1] Create integration tests for CLI with valid basic arithmetic expressions in `tests/integration/test_cli.py`

### Implementation for User Story 1

- [x] T007 [US1] Implement parsing logic for basic arithmetic expressions in `src/calculator/parser.py`
- [x] T008 [US1] Implement evaluation logic for basic arithmetic operations in `src/calculator/evaluator.py`
- [x] T009 [US1] Implement CLI entry point to process and display results for valid basic arithmetic expressions in `src/calculator/main.py`

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Handle Division by Zero (Priority: P1)

**Goal**: As a user, when I attempt to divide by zero, I want the calculator to gracefully handle the operation and provide an informative error message instead of crashing.

**Independent Test**: Can be fully tested by providing expressions involving division by zero (e.g., "10/0") and verifying that an appropriate error message is displayed, and the application remains functional.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [x] T010 [US2] Create unit tests for division by zero handling in `tests/unit/test_evaluator.py`
- [x] T011 [US2] Create integration tests for CLI with division by zero expressions in `tests/integration/test_cli.py`

### Implementation for User Story 2

- [x] T012 [US2] Implement division by zero handling in `src/calculator/evaluator.py`
- [x] T013 [US2] Implement CLI to display division by zero error message in `src/calculator/main.py`

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Handle Invalid Input (Priority: P2)

**Goal**: As a user, when I input an invalid mathematical expression, I want the calculator to provide an informative error message.

**Independent Test**: Can be fully tested by providing various invalid expressions (e.g., "5++3", "abc", "2**3") and verifying that an appropriate error message is displayed.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [x] T014 [US3] Create unit tests for invalid expression parsing in `tests/unit/test_parser.py`
- [x] T015 [US3] Create integration tests for CLI with invalid expressions in `tests/integration/test_cli.py`

### Implementation for User Story 3

- [ ] T016 [US3] Implement invalid expression parsing logic in `src/calculator/parser.py`
- [ ] T017 [US3] Implement CLI to display invalid expression error message in `src/calculator/main.py`

**Checkpoint**: All user stories should now be independently functional

---

## Phase N: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [ ] T018 Review code against Constitution principles in `.specify/memory/constitution.md`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Parser before evaluator
- Core implementation before CLI integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks (T001, T002) can run in parallel if creating separate files/directories.
- Once Foundational phase completes, User Story 1, 2, and 3 can ideally be worked on in parallel by different team members, though sequential completion by priority is recommended for a single developer.
- Within each user story, tasks marked [P] (none currently, but could be if separate files created concurrently) can run in parallel.

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Create unit tests for parsing valid basic arithmetic expressions in `tests/unit/test_parser.py`"
Task: "Create unit tests for evaluating valid basic arithmetic operations in `tests/unit/test_evaluator.py`"
Task: "Create integration tests for CLI with valid basic arithmetic expressions in `tests/integration/test_cli.py`"

# Launch parser and evaluator implementation for User Story 1 (if no direct file conflicts):
Task: "Implement parsing logic for basic arithmetic expressions in `src/calculator/parser.py`"
Task: "Implement evaluation logic for basic arithmetic operations in `src/calculator/evaluator.py`"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
