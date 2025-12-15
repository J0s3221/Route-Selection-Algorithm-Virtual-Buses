# Route Selection Algorithm For Virtual Buses

**This project was developed in the context of the course of Redes Veiculares of Universidade de Lisboa - Instituto Superior Tecnico**

## Introduction

This program implements the selection algorithm for a virtual system of On-Demand public transit system develop as a proof of concept.

**NOTE:** If you don't care about the indepth explanation you can jump to the **Pratical Guide section** that has the instructions on how to run the code and tests.

In this system the buses are always expecting to receive user request for pick-up, they have to take this request and decide if they can take the request. In the case of a bus being already on route the descision will be made by balancing the the current route with the request made by the user, it takes the position of the user and their destination and computes the deviation from current route and grades it in a scale for its affinaty with the current route. In case of a high grade it accepts the request, otherwise it ignores it.

## Design Choices

This section describes the main design decisions adopted in the development of the proof-of-concept (PoC) on-demand public transit system, along with the rationale behind each choice. The goal of the system is to demonstrate decentralized route selection and admission control in a low-density vehicular network environment.

### Decentralized, Bus-Centric Decision Making

The system adopts a fully decentralized architecture in which **each bus independently evaluates pickup–dropoff requests and decides whether to accept or reject them**. This design reflects realistic vehicular network constraints, where on-board units (OBUs) must operate with limited information and low latency.

By delegating route computation and decision-making to individual buses:
- The system avoids centralized bottlenecks.
- Communication overhead is reduced.
- The architecture remains scalable as the number of vehicles increases.

### Problem Scope and Assumptions

The development of this project is based on the following scope and assumptions:

- Operational area modeled as a **100 × 100 two-dimensional grid**
- Target environment characterized as **low-density rural or suburban**
- Absence of traffic congestion, with buses operating at a **constant speed**
- No explicit road network or topology constraints; movement is unconstrained within the grid

These assumptions allow the system to focus on route selection and admission heuristics without interference from traffic dynamics or infrastructure complexity.

## Heuristics and Decision Rules

The system implements a set of lightweight, local heuristics to govern route construction and request acceptance in a low-density on-demand transit scenario.

### Route Representation

- Routes are modeled as an **ordered list of events**
- Each request generates a pickup (PU) and a dropoff (DO)
- A pickup must always precede its corresponding dropoff

---

### Route Insertion

- Incoming requests are evaluated by inserting PU and DO events at all feasible positions in the current route
- The insertion that results in the **minimum marginal increase in route length** is selected
- Route length is computed from the current bus position

---

### Feasibility Rules

- Requests are rejected if the pickup location is beyond a maximum distance from the current bus position
- Requests are rejected if the minimum marginal route extension exceeds a predefined limit

---

### Affinity Scoring

- Each feasible request is assigned a score in the range `[1, 10]`
- The score is derived from the marginal route extension
- Higher scores indicate better compatibility with the current route

---

### Load-Adaptive Admission

- The acceptance threshold increases with the number of planned route events
- Empty or lightly loaded buses are more permissive
- Buses with more scheduled stops become increasingly selective

---

### Acceptance and Idle Behavior

- A request is accepted if its score meets or exceeds the current dynamic threshold
- Accepted requests are inserted into the route; rejected ones are ignored
- When no stops remain, the bus returns to a predefined base location


## Demonstration Scenarios

Here's list and explain the demonstration scenarios and their expected ouput

## Pratical Guide

### How to: Route Algorithm

Here explain how to run the program

### How to: Test Scenarios

Here explain how to run the makefile with the scenarios

## Developers

**José Oliveira - J0s3221**