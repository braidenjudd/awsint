# Observer Pattern

## Overview
An object called the subject creates the ability to register interested observers. The observers are then notified on when the something in the subject changes.

## Advantages
- Decouples the Subject and Observer from each other
- Allows a one to many relationship
- Useful for reacting to events in a system

## Consequences or concerns
- Subject has no idea of the consequences when it changes
- Notifications may be dropped or missed
- Observers may take a long time to process, may need to queue

# Proxy Pattern

## Overview
An object acts as a middle man between two objects. This allows a simple interface to be written for a very complicated object.

## Advantages
- Can create side effects when calls to subject are made, such as caching, logging and counting
- Can simplify or augment an existing object's interface

## Consequences or concerns
- Can hide the fact the subject is beyond the LAN
- Can add unexpected behavior

# Adapter Pattern

## Overview
Like the proxy pattern but the adapter pattern has a specific use case to simplify an interface to an object in an attempt to create a consistent API to a group of different objects.

## Advantages
- Allows you to hide the complexities of disparate objects

## Consequences and concerns
- None as it solves a particular problem