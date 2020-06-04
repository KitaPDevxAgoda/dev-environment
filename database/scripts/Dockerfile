FROM microsoft/mssql-server-linux:latest

ENV SA_PASSWORD=Agoda1234.
ENV ACCEPT_EULA=Y

COPY . .
RUN /opt/mssql/bin/sqlservr & /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P Agoda1234. -d master -i create_table_mail.sql

CMD /opt/mssql/bin/sqlservr