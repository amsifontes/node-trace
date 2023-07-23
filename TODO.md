## Running TODO list

- ~~configure 4 flask applications. each application has /hello-world route that returns hello world. apps 1-3 are test apps, app 4 is metric service~~
- each application loads node trace client as module
- node trace module has own docker for running tests, not run as part of project docker-compose with 4 flask applications
- client module successfully configures web connection from apps 1-3 to app 4 (metric service) and can send requests with json payload
- metric service application can be run as part of docker-compose project and connect to neo4j service
- metric service can send requests to neo4j service
- create model for services (nodes) and message (edges, can be request and response)
- metric service has unit and integration tests (integration tests cover crud operations on )
- sample events can be created
