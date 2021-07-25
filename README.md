# Database Design Pattern

This is a re-implementation of old code (from memory) for database connection and configurations. The code has been refactored for my better understanding of design patterns, the code will continue to change as I further deepen my understanding.

Historically I would just have a function for getting/setting the configurations and credentials for each data source, and a function to get the data based on each configuration.

The code is now refactored into three classes handling the **configuration**, **credential** and **connection** separately. Each task now have abstract classes and can be expanded for additional data sources and configurations, this is a manifestation of the `dependency inversion principle` and the `open-closed principle`. The refactoring also embraces the `single responsibility principle` where the classes has only a single responsibility, for example, instead of getting the configuration and credential then sets the connection string in a single function, they are now handled by their respective code.