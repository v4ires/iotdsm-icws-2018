# IoTDSM - Paper Results (IEEE Services 2018)

> Figures, Scripts, Graphics and Results

This Git repository contains all the data used to generate the results presented in the article submitted at the conference [ICWS 2018](http://conferences.computer.org/icws/2018/), entitled "Performance Evaluation of Strategies for Data Storage and Conversion in IoT". The results refer to the performance evaluation performed on the **I**nternet **o**f **T**hings **D**ata as a **S**ervice **M**odule - IoTDSM. This GIT repository provides the scripts used for chart generation and execution of experiments. To facilitate the installation of Jupyter Notebook, a tool used for charting and statistical analysis, we also provided a Docker image for generating the presented results.

## Installation

To run the docker image, first, we have to compile the Dockerfile file. In this file, all the necessary instructions for container generation are presented. Run the command:

```bash
~$ docker build -f Dockerfile -t iotdsm-services-2018 .
```

After compiling the image, just run the following command to run the Jupyter Notebook.

```bash
~$ docker run -dp 8888:8888 iotdsm-services-2018 jupyter notebook --notebook-dir=/iotdsm-services-2018/ --ip='*' --port=8888 --no-browser --allow-root
```

After executing the command just open the browser and access the URL:

```
http://localhost:8888
```

The notebooks available for execution are:

```bash
doe_results.ipynb 
monitoring_results.ipynb
normality_test.ipynb
response_time_results.ipynb
```

## Authors

Vinícius Aires Barros – [@v4ires](https://scholar.google.com/citations?user=HjQRs4YAAAAJ) – viniciusaires@usp.br

Leonardo Beck Prates – [@leobeckp](https://github.com/leobeckp) – leonardo.prates@usp.br

Sarita Mazzini Bruschi - [@sarita](https://saritabruschi.net/) - sarita@icmc.usp.br

Júlio Cezar Estrella - [@jcezar](https://scholar.google.com/citations?user=uDdnClUAAAAJ) - jcezar@icmc.usp.br

## License

This project is licensed under the MIT license - see the [``LICENSE``](LICENSE) file for more details.

[https://github.com/v4ires/iotdsm-services-2018](https://github.com/v4ires/iotdsm-services-2018)

## Acknowledgments

* Coordination of Improvement of Higher Level Personnel - [CAPES](http://www.capes.gov.br/)
* University of São Paulo - [USP](http://usp.br/)
* Institute of Mathematical and Computer Sciences - [ICMC](http://icmc.usp.br/)
* Laboratory of Distributed Systems and Concurrent Programming - [LaSDPC](http://lasdpc.icmc.usp.br/)