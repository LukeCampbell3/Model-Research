# RBA Update Deprecation Report

Status: `RBA_ROUTE_CONFIDENCE_UPDATE_DEPRECATED`

Do not use the previous in-bounds head plus route-confidence regularization update again as a repair path.
It changed confidence metadata but worsened matched diagnostic loss and reduced route margin.

Recommended replacement: dense approximation first, routing specialization second, efficiency compression third.