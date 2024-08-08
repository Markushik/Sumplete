FROM python:3.12.4 as build

ENV VIRTUAL_ENV=/opt/venv \
    PATH="/opt/venv/bin:$PATH"

RUN apt-get update && \
    apt-get install -y build-essential curl

ADD https://astral.sh/uv/install.sh ./install.sh
RUN chmod -R 655 /install.sh && /install.sh && rm /install.sh

COPY requirements.txt ./

RUN /root/.cargo/bin/uv venv /opt/venv && \
    /root/.cargo/bin/uv pip install --no-cache -r requirements.txt

FROM python:3.12-slim-bookworm

ENV PATH="/opt/venv/bin:$PATH"

COPY --from=build /opt/venv /opt/venv
COPY src ./src/
COPY settings ./settings/

CMD ["/opt/venv/bin/python", "-m", "src.presentation.tgbot"]