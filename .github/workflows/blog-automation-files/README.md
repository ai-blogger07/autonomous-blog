# Autonomous Blogging System

This repository contains a fully automated blogging system that can plan, write, optimize, publish, and promote blog posts using free and open tools/APIs.

## Overview

The system is built on GitHub Pages with Jekyll and includes a comprehensive automation pipeline that handles everything from keyword discovery to social promotion and analytics tracking.

## Features

- **Jekyll Blog Framework**: Ready-to-use blog with customizable theme
- **Automated Content Pipeline**: Python-based system for end-to-end blog post creation
- **GitHub Actions Integration**: Automated deployment workflow
- **SEO Optimization**: Keyword discovery and content optimization
- **Content Creation**: Automated article writing with proper formatting
- **Grammar & Style Checking**: Automated proofreading
- **Visual Generation**: Featured image creation
- **Publishing**: Automated deployment to GitHub Pages
- **Monetization**: Affiliate link integration
- **Social Promotion**: Multi-platform content sharing
- **Email Drafting**: Newsletter creation
- **Analytics**: Performance tracking and reporting

## Getting Started

### Prerequisites

- GitHub account
- Python 3.6+
- Ruby and Jekyll (for local development)

### Setup

1. Fork this repository
2. Update the `config.yaml` file with your blog details and API keys
3. Enable GitHub Pages in your repository settings
4. Optionally configure a custom domain

### Usage

To create a new blog post:

```bash
python src/pipeline/run_pipeline.py "Your blog topic here"
```

## Configuration

All system settings are managed in the `config.yaml` file, including:

- Blog identity and branding
- API keys and credentials
- Content creation parameters
- Publishing preferences
- Monetization settings
- Social promotion options

## Directory Structure

```
blog-automation/
├── _posts/                 # Jekyll blog posts
├── _site/                  # Generated site (not in repo)
├── .github/workflows/      # GitHub Actions workflows
├── src/                    # Source code
│   └── pipeline/           # Automation pipeline modules
├── _config.yml             # Jekyll configuration
├── config.yaml             # Automation system configuration
├── Gemfile                 # Ruby dependencies
└── README.md               # This file
```

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Jekyll for the static site generation
- GitHub Pages for hosting
- Various free APIs that power the automation pipeline
