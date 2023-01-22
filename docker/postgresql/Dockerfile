FROM postgres:13.1

# Copy scripts
COPY ./docker/postgresql/scripts/ /docker-entrypoint-initdb.d/
RUN chmod +x /docker-entrypoint-initdb.d/*.sh