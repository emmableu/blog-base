
```
Trainer.evaluate() ───────────────┐
                                  │
calls → Trainer.evaluation_loop() ───────────────────┐
│                                                    │
│   ┌─────────────────────────────────────────────┐  │
│   │ iterate over dataloader                     │  │
│   │   → call self.prediction_step()             │  │
│   │        └── calls self.compute_loss(...)     │  │
│   └─────────────────────────────────────────────┘  │
│                                                    │
│ collect:                                           │
│  - loss                                            │
│  - logits (model predictions)                      │
│  - labels                                          │
│  - metrics (from compute_loss, if return=True)     │
│                                                    │
│ Finalize:                                          │
│  - gather across processes                         │
│  - truncate extra padding                          │
│                                                    │
└────── calls → self.compute_metrics(...) ←───┐      │
                                              │      │
               (if you set compute_metrics function) │
                                              │      │
    metrics dictionary (e.g. accuracy, F1) ◄──┘      │
                                                     │
Returns: EvalLoopOutput(predictions, labels, metrics)┘
```