# 🗑️ Slack File Cleaner
It is a serverless function that periodically delete old attatchment files.

## Description
Using Slack's LEGACY TOKEN to check old files, and delete them all.
LEGACY TOKEN needs to be create manually, but AWS side automates environment construction by using Serverless Framework.

## Requirement
- AWS Account
- Serverless Framework
- [serverless-plugin-aws-alerts](https://serverless.com/blog/serverless-ops-metrics/) (optional)
- Slack Account / Administrator Role

## Installation
1. Create LEGACY TOKEN from [Here](https://api.slack.com/custom-integrations/legacy-tokens)

2. Clone this repo.
```
$ git clone https://github.com/saitota/SlackFileCleaner.git
```

4. Modify environment_dev.yml 's two TOKEN to your token.
``` environment_dev.yml
LEGACY_TOKEN: 'xoxp-000000000000-000000000000-000000000000-0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x0x'
```

5. Deploy with Serverless Framework (you must aws-cli initialize before)
```
$ sls deploy ./SlackFileCleaner
...
api keys:
  None
endpoints:
  None
functions:
  fnc: SlackFileCleaner-dev-fnc
```
6. Done! Wait a time to archive. (12:30 JST is the default)

# 🤔 Anything Else
I will write article about this function.

[saitotak - Qiita](https://qiita.com/saitotak/)

# 🐑 Author
[saitotak](https://qiita.com/saitotak)

# ✍ License
[MIT](./LICENSE)

