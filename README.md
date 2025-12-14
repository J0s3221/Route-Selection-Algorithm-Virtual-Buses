# Route Selection Algorithm For Virtual Buses

**This project was developed in the context of the course of Redes Veiculares of Universidade de Lisboa - Instituto Superior Tecnico**

## Introduction

This program implements the selection algorithm for a virtual system of On-Demand public transit system develop as a proof of concept.

**NOTE:** If you don't care about the indepth explanation you can jump to the **Pratical Guide section** that has the instructions on how to run the code and tests.

In this system the buses are always expecting to receive user request for pick-up, they have to take this request and decide if they can take the request. In the case of a bus being already on route the descision will be made by balancing the the current route with the request made by the user, it takes the position of the user and their destination and computes the deviation from current route and grades it in a scale for its afinaty with the current route. In case of a high grade it accepts the request, otherwise it ignores it.

To prevent the case of a user not being picked up by any bus for not fitting any current route it is also implemented a hierarchical grading that go's up with time making customers request that are waiting for longer have priority over just requests just made.

This is a proof of concept project, but it is thought out to be implemented in low density constricted areas which would also diminish the just state problem.

## Implementation & Context

Start by explaining the imagened target area and the assumptions made

Then explain the heuristics/rules of decision implemented

Rule the acceptance threshold goes up with the amount of passangers a bus already has, so if it has none all and any path is accepted, this makes for a load-adaptive acceptance policy, which is commonly used in demand-responsive transport to avoid over-committing vehicles.

## Demonstration Scenarios

Here's list and explain the demonstration scenarios and their expected ouput

## Pratical Guide

Here explain how to run the program and tests

## Developers

**José Oliveira - J0s3221**