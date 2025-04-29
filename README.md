# カレンダーアプリ

## 概要
Docker,Git勉強会用のリポジトリ(2025/07/14,2025/07/21)

## 目的
- Dockerを用いた開発をやってみる
- Gitを用いたチーム開発をやってみる

## 使用技術

|  |  |
| ---- | ---- |
| フロントエンド | TypeScript,React,Vite |
| バックエンド | Python,FastAPI |
| データベース | SQL,MySQL |
| コンテナ | Docker |

## 必要な環境変数・APIキー

- .env

    ```
    FRONTEND_PORT=xxx
    BACKEND_PORT=xxx
    DATABASE_PORT=xxx

    MYSQL_DATABASE=xxx
    MYSQL_ROOT_PASSWORD=xxx
    MYSQL_USER=xxx
    MYSQL_PASSWORD=xxx
    MYSQL_HOST=xxx

    GOOGLE_CALENDER_API_KEY=xxx
    VITE_APP_GOOGLE_CALENDER_API_KEY=xxx

    GOOGLE_CALENDER_ID=xxx
    VITE_APP_GOOGLE_CALENDER_ID=xxx
    ```