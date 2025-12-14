# Route Selection Algorithm For Virtual Buses

**This project was developed in the context of the course of Redes Veiculares of Universidade de Lisboa - Instituto Superior Tecnico**

## Introduction

This program implements the selection algorithm for a virtual system of On-Demand public transit system develop as a proof of concept.

**NOTE:** If you don't care about the indepth explanation you can jump to the **Pratical Guide section** that has the instructions on how to run the code and tests.

In this system the buses are always expecting to receive user request for pick-up, they have to take this request and decide if they can take the request. In the case of a bus being already on route the descision will be made by balancing the the current route with the request made by the user, it takes the position of the user and their destination and computes the deviation from current route and grades it in a scale for its affinaty with the current route. In case of a high grade it accepts the request, otherwise it ignores it.

## Implementation & Context

This project is thought out to be flexible to be adapted to different environments, but in this implementation we chose a context of *rural/suburban* area of operation with a low density of population and less traffic constraints. We believe an On-Demand public transit 
C-ITS would display its benefits the most, but other context where this could be useful would be for a first/last mile implementation in a urban residential area.

### Problem Scope and Assumptions

The scope and assumptions taken in the development of this project:
- Operational area: `100 × 100 grid`
- Environment: low-density *rural/suburban*
- Traffic-free, constant-speed buses
- No road constraints

### Rules and Logic

This system implements a Local Decision-Making Model (Bus-Centric). Each bus operates independently, making local decisions upon receiving a pickup–dropoff request, without global optimization or coordination.

Pickup and dropoff requests are processed on-demand

Start by explaining the imagened target area and the assumptions made

Then explain the heuristics/rules of decision implemented

Rule the acceptance threshold goes up with the amount of passangers a bus already has, so if it has none all and any path is accepted, this makes for a load-adaptive acceptance policy, which is commonly used in demand-responsive transport to avoid over-committing vehicles.

## Demonstration Scenarios

Here's list and explain the demonstration scenarios and their expected ouput

## Pratical Guide

### How to: Route Algorithm

Here explain how to run the program

### How to: Test Scenarios

Here explain how to run the makefile with the scenarios

## Developers

**José Oliveira - J0s3221**