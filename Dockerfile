FROM continuumio/anaconda3

EXPOSE 8888

RUN mkdir ~/.jupyter/
RUN touch ~/.jupyter/jupyter_notebook_config.py
RUN echo "c.NotebookApp.token = u''" >> ~/.jupyter/jupyter_notebook_config.py
ADD . $HOME/iotdsm-services-2018

VOLUME /root/iotdsm-services-2018