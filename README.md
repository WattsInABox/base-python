# Triangle, Triangle, What Art Thou, Triangle?

Shakespeare aside, this is Billy Watson's attempt to solve the following problem:

    Write a program in either Python or Java that reads 3 inputs. These inputs represent the lengths of 3 lines. The program must identify the type of triangle (equilateral, scalene, or isosceles) that would be formed by connecting the endpoints of each line.
 
    Published Criteria:
    * The program may read console input or input from a file
    * The program must be production quality

## Setup

1. Install docker
1. (Probably not required) install docker-compose (should come with docker nowadays, upgrade if you don't have it)
1. Use whatever version of python 3 you already have or install one (it really doesn't matter as you will see)
1. Install local requirements

        pip install -r python-requirements/local_requirements.txt

1. Build the containers

        invoke build

1. Run the tests

        invoke test

## Usage

TODO

    invoke execute --

## Tasks

- [ ] constructor for triangle should take 3 sides
- [ ] method should be able to return triangle type
- [ ] CLI should take in 3 sides of a triangle
- [ ] CLI should print triangle type
- [ ] CLI should error out if less than 3 arguments are given
- [ ] CLI should error out if more than 3 arguments are given
- [ ] CLI should error out if any argument is a string
- [ ] CLI should error out if arguments cannot form a triangle
- [ ] triangle type determination should be seperate from the CLI
- [ ] create and document easy usage through `invoke`
- [ ] should allow for more triangle determinations in the future
- [ ] should allow for more triangle specifications in the future


