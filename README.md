# timenote-timeular
Track your time with the Timeular cube and Timenote.

This is a fork of hackaru-timeular by Pascal Wittmann at https://github.com/pSub/hackaru-timeular.

## Motivation

Timeular (https://timeular.com/) offers a hardware and a software component that helps you to keep track of your time. The great thing is, that you can use the hardware without their software. I really like the idea of the hardware cube. It simply is physically present right besides you. When using the Timeular cube, it is rare that I forget to start or stop the timer for a task. If you want to learn more about the tracker, visit https://timeular.com/tracker/.

I have not looked into the time tracking software from Timeular as I already have a Timenote which works really well for me. This led to the creation of `timenote-timeular`, a small Python program that connects a Timeular cube to timenote.

## Installation

`timenote-timeular` is available via PiPy and can be installed as simple as `pip install timenote-timeular`.

## Configuration

`timenote-timeular` is configured in the configuration file `$XDG_CONFIG_HOME/timenote-timeular/config.yml`.

The following example shows how to configure `timenote-timeular` to connect to your Timeular cube and a timenote instance.

```
# The bluetooth address of your Timeular cube
address: 00:11:22:33:FF:EE

# The API URL of the timenote instance
endpoint: "https://api.timenote.app"

# The Email address connected to you timenote account
email: your-email@example.com

# A list of tasks resembling the tasks in your timenote instance
tasks:
  task-1:
    id: 3 # The timenote project id
    description: Describe what you do
  daily:
    id: 4
    description: Daily 
  coding:
    id: 5
    description: Coding

# The mapping of Timeular cube sides to timenote tasks
mapping:
  1: task-1
  2: daily
  3: coding
```

The first time you start `timenote-timeular` you have to enter your password to login. The login information (cookie) is stored at `$XDG_CONFIG_HOME/timenote-timeular/cookies.txt`.