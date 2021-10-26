<p align="center">
  <a href="https://unifai.store"><img src="https://i.ibb.co/XLgpJXc/Capture-d-e-cran-2021-10-06-a-09-10-19.png" alt="UnifAI"></a>
</p>
<p align="center">
  <em>UnifAI the fastest way to develop and deploy AI APIs.</em>
  <br/>
  <em>The fastest way to implement and compare AI research models for a given task.</em>
</p>

---
**Open Source Project Website**: <a href="https://www.unifai.store/" target="_blank">https://www.unifai.store/</a>

**Documentation**: <a href="https://docs.unifai.store/unifai/" target="_blank">https://docs.unifai.store/unifai/</a>

**Documentation Source Code**: <a href="https://github.com/theunifai/unifai-docs/" target="_blank">https://github.com/theunifai/unifai-docs</a>

**Framework Source Code**: <a href="https://github.com/theunifai/unifai-apis-core/" target="_blank">https://github.com/theunifai/unifai-apis-core</a>

**Discord**: <a href="https://discord.com/invite/S9zFnPNG" target="_blank">https://discord.com/invite/S9zFnPNG</a>

---
<p align="left">
    <a href="https://github.com/theunifai/unifai-apis-core/issues" alt="Issues">
        <img src="https://img.shields.io/github/issues/theunifai/unifai-apis-core" /></a>
    <a href="https://github.com/theunifai/unifai-apis-core/pulls" alt="Pull Requests">
        <img src="https://img.shields.io/github/issues-pr/theunifai/unifai-apis-core" /></a>
    <a href="https://github.com/theunifai/unifai-apis-core/network/members" alt="Forks">
        <img src="https://img.shields.io/github/forks/theunifai/unifai-apis-core" /></a>
    <a href="https://github.com/theunifai/unifai-apis-core/stargazers" alt="Stars">
        <img src="https://img.shields.io/github/stars/theunifai/unifai-apis-core" /></a>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![DockerHub](https://dockeri.co/image/unifai/unifai-apis-core)](https://hub.docker.com/repository/docker/unifai/unifai-apis-core)

# Quickstart
## Magic Start
```sh
docker run -d -p 8080:80 unifai/unifai-apis-core:latest
```

## What's behind the Quickstart scene
```sh
git clone https://github.com/theunifai/unifai-apis-core.git
cd unifai-apis-core/api

## DEV ENV
#building the development Docker Image
docker build --target dev -t unifai-apis -f gpu.Dockerfile .
# OR use our magic wrapper
./build_and_dev

## PROD ENV
#building the production Docker Image
docker build --target prod -t unifai-apis -f gpu.Dockerfile .
# OR use our magic wrapper
./build_and_prod
```

# CI
CI power by [CDS](https://github.com/ovh/cds)

# Todo
## Deployment
- [ ] add service
- [ ] helm chart

## Framework
- [ ] hide the mess behind the main.py
- [ ] support Openvino

## other features:
- [ ] train your own (drag+drop)
- [ ] serve your own

## Configuration management
- [ ] make sure customization of prometheus works
- [ ] module activation based on database settings

## Features Front
- [ ] gradio integration
- [ ] SOTA frontend
- [ ] admin panel

## Features Back
- [ ] better model cache management
- [ ] better GPU cache management
- [ ] better dashboard in grafana
- [ ] SOTA qualitative comparer
- [ ] DOI wrapper
- [ ] Arxiv wrapper
- [ ] CPU/GPU switch ? is it possible ?

## SOTA Integration Examples
- [ ] example data for qualitative SOTA from SOTA dataset

## SDK
- [ ] make sure sdk are working

## Usage Examples
- [ ] examples of integrations in javascript
- [ ] examples of integrations in react
- [ ] examples of integrations in python
- [ ] examples of integrations in php
- [ ] examples of integrations in bash
- [ ] examples of integrations in *
- [ ] integration examples

## Documentation
- [ ] changelog

## Community
- [ ] project forum
