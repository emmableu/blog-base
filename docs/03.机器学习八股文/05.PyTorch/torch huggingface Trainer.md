---
title: torch huggingface Trainer
date: 2025-06-15 14:34:26
permalink: /pages/412b34/
categories:
  - 机器学习八股文
  - PyTorch
tags:
  - 
author: 
  name: emmableu
---

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