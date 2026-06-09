# Pvr Ec Nlp Stage2 Model Comparison Report
**Status:** COMPLETE

```json
{
  "status": "COMPLETE",
  "results": {
    "baseline": {
      "compositional_grammar": {
        "final_loss": 0.0006283505936153233,
        "final_accuracy": 1.0,
        "loss_curve_start": 5.124705791473389,
        "loss_curve_end": 0.0006339066312648356,
        "loss_reduction": 0.9998763038002456,
        "converged": true
      },
      "agreement_dependency": {
        "final_loss": 0.00015823330613784492,
        "final_accuracy": 1.0,
        "loss_curve_start": 0.2831338942050934,
        "loss_curve_end": 0.000159192131832242,
        "loss_reduction": 0.9994377496474621,
        "converged": true
      },
      "negation_polarity": {
        "final_loss": 0.0001304430334130302,
        "final_accuracy": 1.0,
        "loss_curve_start": 0.818482518196106,
        "loss_curve_end": 0.00013107182167004794,
        "loss_reduction": 0.9998398599618732,
        "converged": true
      },
      "ambiguous_word_sense": {
        "final_loss": 0.0021138754673302174,
        "final_accuracy": 1.0,
        "loss_curve_start": 1.1719393730163574,
        "loss_curve_end": 0.0021159022580832243,
        "loss_reduction": 0.9981945292505727,
        "converged": true
      },
      "coreference_memory": {
        "final_loss": 0.059596266597509384,
        "final_accuracy": 0.76953125,
        "loss_curve_start": 2.080195903778076,
        "loss_curve_end": 0.05992858111858368,
        "loss_reduction": 0.9711908955258778,
        "converged": true
      },
      "instruction_micro": {
        "final_loss": 0.16285943984985352,
        "final_accuracy": 0.6962617039680481,
        "loss_curve_start": 3.2266790866851807,
        "loss_curve_end": 0.16063721477985382,
        "loss_reduction": 0.9502159308489277,
        "converged": true
      },
      "multisentence_delimiter": {
        "final_loss": 0.30114778876304626,
        "final_accuracy": 0.5681818127632141,
        "loss_curve_start": 3.168260335922241,
        "loss_curve_end": 0.2980145514011383,
        "loss_reduction": 0.9059374799405838,
        "converged": true
      },
      "paraphrase_invariance": {
        "final_loss": 0.017533468082547188,
        "final_accuracy": 0.9320388436317444,
        "loss_curve_start": 1.8876142501831055,
        "loss_curve_end": 0.017678752541542053,
        "loss_reduction": 0.9906343403903487,
        "converged": true
      }
    },
    "warmup_plus_family_align": {
      "compositional_grammar": {
        "final_loss": 0.0013204488204792142,
        "final_accuracy": 1.0,
        "loss_curve_start": 5.124705791473389,
        "loss_curve_end": 0.0045142094604671,
        "loss_reduction": 0.999119128074049,
        "converged": true
      },
      "agreement_dependency": {
        "final_loss": 0.0001527013664599508,
        "final_accuracy": 1.0,
        "loss_curve_start": 0.35557425022125244,
        "loss_curve_end": 0.00042979238787665963,
        "loss_reduction": 0.9987912724624766,
        "converged": true
      },
      "negation_polarity": {
        "final_loss": 0.00019452061678748578,
        "final_accuracy": 1.0,
        "loss_curve_start": 0.7010135650634766,
        "loss_curve_end": 0.0003998110769316554,
        "loss_reduction": 0.9994296671321967,
        "converged": true
      },
      "ambiguous_word_sense": {
        "final_loss": 0.011125077493488789,
        "final_accuracy": 0.9368420839309692,
        "loss_curve_start": 1.1572984457015991,
        "loss_curve_end": 0.01141301915049553,
        "loss_reduction": 0.9901382230375532,
        "converged": true
      },
      "coreference_memory": {
        "final_loss": 0.042225342243909836,
        "final_accuracy": 0.8359375,
        "loss_curve_start": 1.5730177164077759,
        "loss_curve_end": 0.042326539754867554,
        "loss_reduction": 0.9730921404677332,
        "converged": true
      },
      "instruction_micro": {
        "final_loss": 0.2143499255180359,
        "final_accuracy": 0.5934579372406006,
        "loss_curve_start": 3.423311710357666,
        "loss_curve_end": 0.21566647291183472,
        "loss_reduction": 0.9370006323819977,
        "converged": true
      },
      "multisentence_delimiter": {
        "final_loss": 0.2891141176223755,
        "final_accuracy": 0.6079545617103577,
        "loss_curve_start": 3.387547254562378,
        "loss_curve_end": 0.29489150643348694,
        "loss_reduction": 0.9129483711153181,
        "converged": true
      },
      "paraphrase_invariance": {
        "final_loss": 0.016668643802404404,
        "final_accuracy": 0.9563106894493103,
        "loss_curve_start": 1.19906485080719,
        "loss_curve_end": 0.016918133944272995,
        "loss_reduction": 0.9858905596866725,
        "converged": true
      }
    },
    "contrastive_light": {
      "compositional_grammar": {
        "final_loss": 0.005105346441268921,
        "final_accuracy": 0.9955357313156128,
        "loss_curve_start": 5.124705791473389,
        "loss_curve_end": 0.006823588628321886,
        "loss_reduction": 0.998668491635232,
        "converged": true
      },
      "agreement_dependency": {
        "final_loss": 0.00014487486623693258,
        "final_accuracy": 1.0,
        "loss_curve_start": 0.3562747538089752,
        "loss_curve_end": 0.0002798239584080875,
        "loss_reduction": 0.9992145838137099,
        "converged": true
      },
      "negation_polarity": {
        "final_loss": 0.015749100595712662,
        "final_accuracy": 0.898876428604126,
        "loss_curve_start": 0.7814839482307434,
        "loss_curve_end": 0.016209498047828674,
        "loss_reduction": 0.9792580537520617,
        "converged": true
      },
      "ambiguous_word_sense": {
        "final_loss": 0.00019437383161857724,
        "final_accuracy": 1.0,
        "loss_curve_start": 1.0945427417755127,
        "loss_curve_end": 0.00024005831801332533,
        "loss_reduction": 0.9997806770728533,
        "converged": true
      },
      "coreference_memory": {
        "final_loss": 
```