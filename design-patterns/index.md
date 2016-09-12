# Design Patterns the fun way

## Creational patterns

### Factory
*** Don't build a car yourselves. Tell us what type of car you want, we'll build it for ya***

Quite often we need different type of implementations ( cars ) with the same interface ( steering wheel ). The creation of these implementations is hidden inside *Factory*, so that users are unaware of how they're created - they just enjoy using them 

### Singleton
***There's only one bus in town fellas, use it for commuting***

Sometimes, we just want to limit the number of object of a certain type to one, so that it could be shared by all other objects if required.

## Structural patterns
### Adapter
***I have no idea what this guy is saying, get me a translator !***

If two objects ( or systems ) have different and incmpatible interfaces, and still  want to talk, place a middle man that can translate the communication back and forth.


### Composite
***Don't talk to soldiers, talk to their captain***

When we want to treat a group of similar objects into one unit, we make a *composite* out of them. Composite makes sure that anything passed to it reaches to everyone in the group

## Behavioural patterns

### Observer
***Leave your number, we'll call you***

When systems want to get notified of some interesting events, they can register themselves to systems that will notify them later when events happen. 

### Facade
***There is just a single manager to a fifty member team***

Usually there exist multiple tightly-coupled god-only-understands spaghetti-styled objects in a system, but the clients want a simpler interface to talk to. *Facade* is that interface

## Concurrency patterns
