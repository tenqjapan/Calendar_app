# カレンダーアプリ

## 概要
Docker,Git勉強会用のリポジトリ(2025/07/14,2025/07/21)

## 目的
- Dockerを用いた開発をやってみる
- Gitを用いたチーム開発をやってみる
- 中山研のイベントをまとめたカレンダーアプリを作成したい

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
    FRONTEND_PORT=xxx //フロントエンドコンテナ用のポート番号
    BACKEND_PORT=xxx //バックエンドコンテナ用のポート番号
    DATABASE_PORT=xxx //データベースコンテナ用のポート番号

    MYSQL_DATABASE=xxx //データベース名
    MYSQL_ROOT_PASSWORD=xxx //ルートユーザーのパスワード
    MYSQL_USER=xxx //一般ユーザー名
    MYSQL_PASSWORD=xxx //一般ユーザー名のパスワード
    MYSQL_HOST=xxx //ホストのURL(Dockerを使用する場合はコンテナ名を指定する)

    GOOGLE_CALENDER_API_KEY=xxx //GoogleカレンダーのAPIキー
    VITE_APP_GOOGLE_CALENDER_API_KEY=xxx //GoogleカレンダーのAPIキー(Viteで利用するためVITE_APP_をつけたもの)

    GOOGLE_CALENDER_ID=xxx //GoogleカレンダーのID
    VITE_APP_GOOGLE_CALENDER_ID=xxx //GoogleカレンダーのID(Viteで利用するためVITE_APP_をつけたもの)
    ```

## 環境構築

0. Docker,Gitを使用できる状態にしておく

1. 本リポジトリを任意のディレクトリにクローンする

    ```git clone git@github.com:shunsuke-kawata/calender_app.git```

2. 環境変数を設定する

   1. 環境変数に必要な値を取得する
   
       - `GOOGLE_CALENDER_API_KEY`はGoogle Cloud PlatformコンソールからAPIキーを発行して取得
       - `GOOGLE_CALENDER_ID`はGoogleカレンダーを作成して設定から取得
   2. `.env`をこのリポジトリのルートに作成して[必要な環境変数・APIキー](#必要な環境変数・APIキー)を参照し必要な情報を記載する

3. Dockerコンテナを作成
   
   ```docker compose build``` Dockerイメージを作成

   ```docker compose up``` Dockerコンテナの起動

   ```docker compose up --build``` 上記二つを同時実行

4. 起動を確認する
   
   ```http://localhost:{FRONTEND_PORT}```でReactによるフロントエンドが起動

   ```http://localhost:{BACKEND＿PORT}```でFastAPIによるバックエンドが起動
