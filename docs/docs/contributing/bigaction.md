# BigAction
## Introduction
Welcome to the BigAction section of our contributing guide!

[BigAction](https://huggingface.co/BigAction) is an open source initiative to collect datasets used to train and evaluate Large Action Models (LAMs).

Development of reliable LAMs is a challenge that requires high-quality curated data representing a wide diversity of actions.

Take a look at our two publicly available datasets: 

- [the-wave-clean](https://huggingface.co/datasets/BigAction/the-wave-clean): a curated, handbuilt, dataset of (query, page HTML) -> (Selenium code)  
- [mind2web_clean](https://huggingface.co/datasets/BigAction/mind2web_clean): mind2web is an open dataset for building web agents and mind2web_clean is our first community contribution! Imène, a PhD student from France, adapted this dataset to map actions to Selenium code. 

BigAction just launched and we're currently looking to build datasets or convert existing ones. This means that current contributions (apart from increasing your telemtry level when using LaVague) require a **high level of involvment** to be meaninful while we build tools to make it easier.

We're essentially looking gather more data that maps a natural language query + the full page HTML to a specific targetable element (xpath, Selenium code, specific html element, etc.)

## Getting started
### Prerequisites
Before contributing to BigAction, you should have a basic understanding of our project's goals and structure. You should also read our [blog post announcing BigAction](https://blog.lavague.ai/announcing-bigaction/) to learn more about our mission with this project. 

### Setup
For now, contributing to BigAction does not require any particular setup. In the next steps we'll show the two main ways you can help us on this project. 

## How to contribute
### 📐 Increasing telemetry: an easy way to contribute to BigAction
One easy way to contribute to improving the quality of our datasets is to increase the telemetry you send us. More telemetry means we'll be able to build a more diverse set of queries and expected results. 

By default, all users have telemetry set to ```LOW``` but you can choose to contribute to usage data by setting it to ```MED``` or ```HIGH```

To learn more about our telemetry and set it to a higher level, see [our dedicated page](../advanced/telemetry.md). We thank you in advance for contributing to the data used to make better web agents. 

### 📊 More involved contributions
Here are some initial areas where we could use your help:

- Convert existing datasets
- Enrich existing datasets
- Help us build an annotation interface to make contributions easier
- Join the community and share your thoughts and ideas 


### Examples
Thanks to Imène, a PhD student from Lyon (France), we now have mind2web_clean. She converted mind2web, a public dataset of high level browser actions, into lower level instructions that help us better target elements in the DOM. 

## Best practices
As we build tools to make contributions easier, you should come discuss how we could best help each other building performant and reliable web agents for everyone. 

### FAQ
Coming soon.

### Need help ?
Join our [Discord](https://discord.gg/invite/SDxn9KpqX9) to ask us any questions!

