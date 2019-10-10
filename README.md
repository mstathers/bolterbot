### BolterBot

A reddit bot that will be used to respond to hobby modeling threads to suggest that people drill out their gun barrels. Will be ran out of AWS lambda and will take a thread url as input.

#### Setup

```
mkvirtualenv -p python3 bolterbot
workon bolterbot
make init
```

#### Usage

You can can deploy to lambda with `make deploy` and run a local test with `make invoke`. If you are deploying you will need tosetup an appropriate IAM user and role - follow online documentation.
