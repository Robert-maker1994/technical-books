## Event-Driven Architecture Cheat Sheet

**Key Concepts**

* **Event-Driven Architecture (EDA):** An architecture style where components communicate through asynchronous events.
* **Event:** A significant change in state.
* **Event Producer:** Emits events.
* **Event Processor:** Receives and processes events.
* **Event Broker:** A message broker that routes events.
* **Topic:** A channel where events are published.
* **Queue:** A channel where events are stored until processed.

**EDA Topologies**

* **Broker Topology:**
    * Events are routed through a central event broker.
    * Event processors subscribe to topics and receive events.
    * Good for complex workflows requiring orchestration.
* **Mediator Topology:**
    * A central mediator component orchestrates event processing.
    * Mediator receives the initial event and sends events to dedicated event channels.
    * Good for simpler event processing flows.

**Communication Styles**

* **Asynchronous:**
    * The producer doesn't wait for the consumer to process the event.
    * Improves responsiveness.
    * Error handling is more complex.
* **Request-Reply:**
    * A form of asynchronous communication that facilitates a response.
    * Uses request and reply queues.

**Error Handling**

* **Workflow Event Pattern:**
    * Delegates error handling to a workflow processor.
    * Aims for resiliency without sacrificing responsiveness.

**Preventing Data Loss**

* **Persistent Message Queues:** Store messages until they are successfully processed.
* **Synchronous Send:** Producer waits for acknowledgment that the message is persisted.
* **Client Acknowledge Mode:** Messages are kept in the queue until the client confirms processing.

**Key Architecture Characteristics**

* Scalability
* Elasticity
* Responsiveness

**When to Use EDA**

* Real-time data processing.
* Decoupled systems.
* Complex event processing.

**Important Notes:**

* Choose the right topology based on workflow complexity.
* Asynchronous communication is a core principle.
* Error handling requires careful consideration.
* Data loss prevention is crucial.
