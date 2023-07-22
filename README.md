# Project NodeTrace

A framework for transparently and contextually inspecting the flow of requests and responses between services within a system by representing those services as nodes, and each request/response as a directed edge, complete with the contents of the request, and metadata such as the time the request/response was initiated and recieved, a unifying transaction id, and optional additional data such as user or session tokens, feature flag states, etc. Servives represented as nodes are abstract and can be as broad as full applications and 3rd party endpoints, or as granular as individual functions within a service.

Possible alternative names:

- LogGraph
- ServiceGraph
- ServiceTrace
- LogTrace
- RequestFlow
- GraphTrace
- ClearGraph
- ClearTrace
- ClearNode

```
 {request_meta:..., sent: t=0, req_id: 123456}
              |
         ------------------->
service 1                    service 2
         <-------------------
                       |
            {request_meta:..., sent: t=1, req_id: 123456}
```
