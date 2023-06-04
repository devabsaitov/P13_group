FROM python:3.11-alpine

RUN mkdir /apps
WORKDIR /apps
COPY . .
RUN --mount=type=cache,id=custom-pip,target=/root/.cache/pip pip install -r req.txt
 #sysctl vm.overcommit_memory=1
#RUN sed -i 's/\r$//g' /apps/entrypoint.sh
#RUN chmod +x /apps/entrypoint.sh
#
#ENTRYPOINT ["/apps/entrypoint.sh"]
