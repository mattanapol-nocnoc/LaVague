# General contribution guidelines

## 🪲 Reporting bugs

We track bugs using [GitHub issues](https://github.com/lavague-ai/LaVague/issues/).

You can report a bug by opening a [new issue](https://github.com/lavague-ai/LaVague/issues/new/choose) using the 'bug report' template.

Please check that your bug has not already been reported before submitting a bug report and include as many details as possible to help us fix bugs faster!

## 💡Suggesting new features

You can make a [new feature request](https://github.com/lavague-ai/LaVague/issues/new/choose) by creating a new issue and selecting the 'new feature' template.

Please provide as much information as possible: the behavior you want, why, and examples of how this feature would be used!

## 👩‍💻 Code contribution process

To avoid having multiple people working on the same things & being unable to merge your work, we have outlined the following contribution process:

- 📢 We outline tasks on our backlog: we recommend you check out issues with the help-wanted labels & good first issue labels
- 🙋‍♀️ If you are interested in working on one of these tasks, comment on the issue!
- 🤝 We will discuss with you and assign you the task with a community assigned label
- 💬 We will then be available to discuss this task with you
- 🍴 [Fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) the LaVague repo!
- ⬆️ When you are ready, submit your work for review by [opening a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)
- ✅ We will review & merge your code or request changes/give feedback

!!! tip "QA"
    When submitting a PR, please:

    - Use a descriptive title
    - [Link](https://docs.github.com/en/issues/tracking-your-work-with-issues/linking-a-pull-request-to-an-issue) to the issue you were working on in the PR
    - Add any relevant information to the description that you could help us review your code
    - [Rebase your branch](https://docs.github.com/en/get-started/using-git/about-git-rebase) against the latest version of `main`.
    - Check your branch passes all GitHub actions pass.

> If you want any help or guidance on developing the feature you are working on more before submitting, reach out to us on [Discord](https://discord.gg/SDxn9KpqX9)!

⚠️ Note, we aim to merge as many PRs as possible but we cannot guarantee to merge PRs and they are subject to our review process.

## Dev environment

1) To get started working locally on LaVague, firstly make sure you have have forked and cloned the LaVague repo:

```bash
git clone https://github.com/USER_NAME/LaVague
```

2) Next, install poetry, our recommended local package manager.

For Linux users with debian-based distributions, you can run:
```bash
sudo apt update
sudo apt install pipx
pipx install poetry
```

> For installation on other Linux distributions or operating systems, see [the officia Poetry installation guide](https://python-poetry.org/docs/#installing-with-pipx).

3) You can now install the lavague package from the root of your forked repo:

```bash
poetry install
```

Your local package will automatically be updated with you latest local file modifications so you can easily test your changes as you work.

!!! "LaVague package structure"
    Note, LaVague is split into various sub-packages to ease issues relating to dependency conflicts. 
    
    The LaVague repo is made up of many subpackages. If you are modifying a subpackage outside of our default `lavague.core` package such as `lavague.gradio`, you will need to run `poetry install` within this specific folder to see your changes.