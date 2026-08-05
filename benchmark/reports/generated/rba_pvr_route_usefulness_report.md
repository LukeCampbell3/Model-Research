# RBA-Inspired PVR Route-Usefulness Report

RBA-inspired PVR route-usefulness result:

1. Repository integration:
   status: COMPLETED
   evidence: Path mapping and alias reports were generated under benchmark/reports/generated.
   caveat: Integration follows the current benchmark/model_factory layout, not a separate router package.

2. In-bounds probability head:
   status: IMPLEMENTED_BUT_NOT_EFFECTIVE_FOR_LOSS
   evidence: The head emits bounded probabilities and the regularized run increased mean owner in-bounds from 0.538915 to 0.585626.
   caveat: Higher confidence did not translate into lower loss.

3. Margin-aware challenger maps:
   status: DIAGNOSTIC_ONLY
   evidence: Score-only challenger maps and route bucket reports were generated.
   caveat: No extra challenger experts were executed.

4. Oracle challenger evaluation:
   status: NOT_RUN_NOT_IMPLEMENTED
   evidence: Offline-only oracle placeholder report is present.
   caveat: No owner-vs-challenger loss deltas are available yet.

5. ResidualMiner diagnostic:
   status: DIAGNOSTIC_ONLY
   evidence: Residual cluster, owner, descriptor/operator, and split-candidate files were generated.
   caveat: It recommends only offline candidates and does not mutate architecture.

6. Route-confidence regularization:
   status: RBA_ADDITIONS_NOT_EFFECTIVE_UNDER_MATCHED_ABLATION
   evidence: Matched 100M intervention: final train loss delta=0.028739, mean eval loss delta=0.144725, final eval loss delta=0.019211.
   caveat: This was a 1000-step / 256k-token diagnostic budget, not a full 4000-step tier.

7. Route-loss predictiveness:
   status: NOT_SUPPORTED_UNDER_MATCHED_ABLATION
   evidence: Regularized confidence/loss correlation over active steps was -0.03835492312338522; route margin regressed by -0.100828.
   caveat: This does not rule out other weights/schedules, but it rules out the implemented 0.01 regularizer as an effective repair in this run.

Hard Top1 invariants:
   status: COMPLETED
   evidence: owners_per_token=1.0, Top2/Top4/runtime dynamic execution counts remained zero, production_map_mutated=false.

Loss-win support:
   status: NOT_SUPPORTED
   evidence: Regularized run was worse than baseline on final train loss, mean last-100 train loss, best eval loss, mean eval loss, and final eval loss.
   caveat: Existing 300M PVR full still beats shared-only, but the RBA additions did not improve that in the matched intervention.

Final conclusion:
   RBA_PVR_ROUTE_USEFULNESS_NOT_SUPPORTED
