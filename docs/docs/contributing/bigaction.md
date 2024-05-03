# BigAction
## Introduction
Welcome to the BigAction section of our contributing guide!

[BigAction](https://huggingface.co/BigAction) is an open-source initiative to collect datasets used to train and evaluate Large Action Models (LAMs). 

The development of reliable LAMs is a challenge that requires high-quality curated data representing a wide diversity of actions as well as methods to measure the performance and reliability of models.

This project is inspired by [BigCode](https://www.bigcode-project.org/). Our ambition is to foster an open collaboration around Large Action Models, just like BigCode did around LLMs for code generation. 

Take a look at our two publicly available datasets:

- [the-wave-clean](https://huggingface.co/datasets/BigAction/the-wave-clean): a curated, handbuilt, dataset of (query, page HTML) -> (Selenium code)  
- [mind2web_clean](https://huggingface.co/datasets/BigAction/mind2web_clean): mind2web is an open dataset for building web agents and mind2web_clean is the first community contribution to BigAction! Imène, a PhD student from France, adapted the original dataset of high-level browser tasks to more detailed actions and the associated Selenium code. 

BigAction just launched and current contributions (apart from increasing your telemetry level when using LaVague) require a **higher level of involvement** to be meaningful while we build tools to make it easier.

## Diving deeper: the-wave dataset

We're essentially looking to gather precise mappings between a pair consisting of a natural language query and the full HTML to a specific HTML element on the page. 

Our first deliverable for BigAction is the the-wave dataset, here is the current schema: 

- **query**: the query to be performed by the agent
- **url**: website where the action should be performed
- **html**: the complete HTML of the page
- **selenium_ground_truth**: a piece of code that targets the element to be interacted with
- **ground_truth_outer_html**: the outer HTML of the element to be interacted with
- **ground_truth_highlighted_screenshot**: a screenshot with a bounding box highlighting the element to be interacted wit



## Getting started
### Prerequisites
Before contributing to BigAction, you should have a basic understanding of our project's goals and structure. You should also read our [blog post announcing BigAction](https://blog.lavague.ai/announcing-bigaction/) to learn more about our mission. 

### Setup
If you want to contribute to our datasets or submit a new one, you will need to [create an account on Hugging Face](https://huggingface.co/join) to submit pull requests.

[Git](https://git-scm.com/book/en/v2/Getting-Started-About-Version-Control) understanding is also valuable since all of our datasets are versioned.

## How to contribute
### 📐 Increase telemetry level
One of the best ways to contribute to improving our datasets is simply to increase the telemetry you send to us and keep trying LaVague on your use cases! More telemetry means we'll be able to build a more diverse set of queries and expected results. 

By default, all users have telemetry set to ```LOW``` but you can choose to contribute to usage data by setting it to ```MED``` or ```HIGH```

To learn more about our telemetry and set it to a higher level, see [our dedicated page](../advanced/telemetry.md). We thank you in advance for contributing to the data used to make better web agents.


### 🏆 Define methods for benchmarking LAMs
Todo Paul: add some more details about what we've done so far

### 📊 Convert and enrich existing datasets
Several public datasets can contain helpful information to build better LAMs and browser agents. 

For example, [mind2web](https://osu-nlp-group.github.io/Mind2Web/) contains a wide variety of tasks on diverse websites. Unfortunately, queries in this dataset are very high level while we're looking for more granular interactions (and their associated targetable elements or code that targets those elements). 

A LaVague community member (Imène, a PhD student from France) has done an amazing job of converting this dataset into more detailed, lower-level instructions.

Todo Paul: add some details about how this dataset was converted. 

If you come across interesting datasets, join our [dedicated channels on the LaVague discord](https://discord.gg/invite/SDxn9KpqX9) to discuss your findings!


### 📝 Build tools to make annotation easier
While we gather some telemetry from LaVague's users, our engine sometimes incorrectly flags an action as successful. Human annotation could help us get additional feedback on whether or not this "successful" interaction was the intended behavior or not. 

To make this a reality, we need a set of tools and interfaces to help annotation. You can draw inspiration from the [prompt-collective](https://huggingface.co/spaces/DIBT/prompt-collective) project and come up with ways of creating more precise labeled data.



## Ready to contribute ?
[Join our community on Discord](https://discord.gg/invite/SDxn9KpqX9) to share your thoughts and ideas on growing the BigAction initiative!

