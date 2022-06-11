# Machine Learning Engineer technical challenge

## Task

### Coding

Add or update modules, methods, snippets or files in order to implement a RESTful API providing the below functionalities:

- Photo API: extract human face(s) locations, if any, from an image
- Audio API: extract non-silent chunks from an audio file
- Text API: extract named entities (English) from a text file

_Endpoints paths, input and output formats are a free choice._

You can add any external dependency unless it is a wrapper for, or it uses, an online service. Solution is meant to work on premises
and thus, will be tested in an offline environment.

### Packaging

Write and use the _Dockerfile_ to ship this to production.

Product should serve functionalities as APIs using a production application server, and to be proxied using a web
server ([nginx](conf/challenge.nginx)).

## Submission

Your solution should consist of both project repository and Docker image.

_Sharing any piece of information outside the private project will not be
considered and could lead to user ban._

### Duration

Solution must be submitted in less than **3 days** after your first access to the challenge link.



## Bonus

Extra points can be earned from doing any of the below:

- Extending Photo API to support PDF input
- Extending Audio API to return chunks timings (start/end)
- Extending Text API to support Arabic text
- Implementing unit and API tests in [test directory](tests)
- Not putting source code inside Docker image


docker-machine create -d virtualbox --virtualbox-memory=2048 --virtualbox-cpu-count=2 --virtualbox-disk-size=20480 --virtualbox-no-vtx-check default
docker run

host/7000
ps
push docker to github