# Transactional Saga Architecture Patterns – Chapter 12 Summary






| Saga Pattern               | Comm.     | Consistency | Coordination  | Coupling     | Complexity  | Responsiveness | Scale/Elasticity |
|---------------------------|-----------|-------------|----------------|--------------|-------------|----------------|------------------|
| **Epic Saga (sao)**       | Sync      | Atomic      | Orchestrated   | Very High    | Low         | Low            | Very Low         |
| **Phone Tag Saga (sac)**  | Sync      | Atomic      | Choreographed  | High         | High        | Low            | Low              |
| **Fairy Tale Saga (seo)** | Sync      | Eventual    | Orchestrated   | High         | Very Low    | Medium         | High             |
| **Time Travel Saga (sec)**| Sync      | Eventual    | Choreographed  | Medium       | High        | Medium         | Medium           |
| **Fantasy Fiction (aao)** | Async     | Atomic      | Orchestrated   | High         | Medium      | Medium         | Medium           |
| **Horror Story (aac)**    | Async     | Atomic      | Choreographed  | Very High    | Very High   | Low            | Low              |
| **Parallel Saga (aeo)**   | Async     | Eventual    | Orchestrated   | Low          | Low         | High           | High             |
| **Anthology Saga (aec)**  | Async     | Eventual    | Choreographed  | Very Low     | High        | High           | Very High        |

> **Legend**:
> - **Comm.** = Communication (Sync = Synchronous, Async = Asynchronous)
> - **Coordination** = Orchestrated (central mediator) or Choreographed (distributed coordination)
> - **Coupling** includes semantic, temporal, and transactional

What is Sync vs Async? 

what is the meaning of Atomic vs Eventual? 

what is Orchestrated vs choreographed? 

