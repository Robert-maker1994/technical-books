Diagramming Architecture

Diagramming is a critical skill for architects as it captures the structure of a system and fosters a shared understanding within a team.

\* Tools: While sophisticated diagramming tools are powerful, the book emphasizes starting with low-fidelity artifacts (like whiteboards or tablets with projectors) early in the design process to encourage iteration and prevent "Irrational Artifact Attachment" (an anti-pattern where attachment to an artifact is proportional to the time invested in creating it). Key features to look for in diagramming tools include:

\* Layers: For logically grouping and hiding/showing elements to manage complexity.

\* Stencils/Templates: To build libraries of common visual components for consistency and faster diagram creation.

\* Magnets: To assist in automatically connecting lines between shapes.

\* Diagramming Standards:

\* UML (Unified Modeling Language): Historically unified competing design philosophies, but mainly UML class and sequence diagrams are still widely used.

\* C4: A diagramming technique by Simon Brown (Context, Container, Component, Class) that aims to modernize UML and is suitable for monolithic architectures.

\* ArchiMate: An open-source enterprise architecture modeling language from The Open Group, designed to be concise for enterprise ecosystems.

\* Diagram Guidelines: Regardless of the tool or standard, effective diagrams should have:

\* Titles: Clear and concise titles for all elements.

\* Lines: Thick enough lines, with arrows indicating information flow and consistency (e.g., solid for synchronous, dotted for asynchronous communication).

\* Shapes: Consistent use of shapes, though no pervasive standard exists.

\* Labels: Label every item, especially if ambiguity is possible.

\* Color: Use color strategically to distinguish artifacts.

\* Keys: Include a key if shapes or colors are ambiguous.

\* Representational Consistency: This practice ensures viewers understand the context of what is being presented by always showing the relationship between parts of an architecture (e.g., drilling down from a high-level topology to specific details).

Presenting Architecture

Effective presentations are crucial for architects to convey their vision and convince stakeholders.

\* Manipulating Time: Presentation tools (like PowerPoint/Keynote) can manipulate time using transitions (slide-to-slide movement) and animations (movement within a slide). These should be used subtly to stitch ideas together and clearly mark topic changes.

\* Incremental Builds: Avoid the "Bullet-Riddled Corpse" anti-pattern where slides are overloaded with text. Instead, use incremental builds to reveal information (ideally graphical) piece by piece, maintaining audience engagement and allowing the presenter to leverage both verbal and visual communication channels effectively.

\* Infodecks Versus Presentations:

\* Infodecks are slide decks meant to be read independently (like a magazine article), containing all necessary information and no time-based elements.

\* Presentations are designed to be delivered with a speaker, where the slides represent only half of the content, with the other half coming from the presenter's verbal explanation.

\* Invisibility: A "blank black slide" can be used to refocus audience attention solely on the speaker for emphasizing a critical point, as it turns off the visual information channel.

By mastering these diagramming and presentation techniques, architects can effectively communicate complex ideas, gain support for their designs, and lead teams successfully through implementation.


### Anti-pattern

\* Irrational artifact Attachment: The anti-pattern occurs in the process of making a diagraming that an architect could become overly attached to, such as whiteboard drawings or early sketches. This can lead to resistance of necessary changes

