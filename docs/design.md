# Design Diagrams

These diagrams describe the current Word Scramble Challenge program.

## 1. System Architecture

```mermaid
flowchart TD
    U[Player] --> M[main.py]
    M --> G[game_logic.py]
    G --> W[word_bank.py]
    G --> I[input_handler.py]
    G --> UT[utils.py]
    G --> S[score_manager.py]
    M --> I
    M --> S
```

## 2. Workflow Diagram

```mermaid
flowchart TD
    A([Start]) --> B[Display welcome message]
    B --> C[Choose difficulty]
    C --> D[Select 5 random words]
    D --> E[Scramble a word]
    E --> F[Enter answer]
    F --> G{Correct?}
    G -- Yes --> H[Add 1 point]
    G -- No --> I{Attempts left?}
    I -- Yes --> F
    I -- No --> J[Show correct word]
    H --> K{More words?}
    J --> K
    K -- Yes --> E
    K -- No --> L[Show game score]
    L --> M{Play again?}
    M -- Yes --> C
    M -- No --> N[Show final score]
    N --> O([End])
```

## 3. Use Case Diagram

```mermaid
flowchart LR
    P[Player]
    P --> A[Select difficulty]
    P --> B[View scrambled word]
    P --> C[Enter answer]
    P --> D[View score]
    P --> E[Play again]
```

## 4. Sequence Diagram

```mermaid
sequenceDiagram
    actor Player
    participant Main as main.py
    participant Game as game_logic.py
    participant Words as word_bank.py
    participant Input as input_handler.py
    participant Utils as utils.py
    participant Score as score_manager.py

    Player->>Main: Start program
    Main->>Game: play_game()
    Game->>Utils: choose_difficulty()
    Utils-->>Game: difficulty
    Game->>Words: Get words for difficulty
    Words-->>Game: Word list
    Game->>Utils: scramble_word(word)
    Utils-->>Game: scrambled word
    Game->>Input: get_answer()
    Input-->>Game: player answer
    Game->>Score: show_game_result()
    Score-->>Player: Game score
    Game-->>Main: score
    Main->>Input: get_replay_choice()
    Input-->>Main: y/n
```

## 5. Component/File Relationship

```mermaid
flowchart TD
    MAIN[main.py]
    GAME[game_logic.py]
    WORD[word_bank.py]
    UTIL[utils.py]
    INPUT[input_handler.py]
    SCORE[score_manager.py]
    TEST[test_game.py]

    MAIN --> GAME
    MAIN --> INPUT
    MAIN --> SCORE
    GAME --> WORD
    GAME --> UTIL
    GAME --> INPUT
    GAME --> SCORE
    TEST --> WORD
    TEST --> UTIL
    TEST --> INPUT
```

## Storage Design

A database is **not applicable** to this project. The words are stored in Python lists inside `word_bank.py`, so no ER diagram or database schema is required.
