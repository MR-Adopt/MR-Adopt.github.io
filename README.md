<!-- ---
title: MR-Adopt: Automatic Deduction of Input Transformation Function for Metamorphic Testing
--- -->

## Welcome to MR-Adopt's Site！
----

The paper “MR-Adopt: Automatic Deduction of Input Transformation Function for Metamorphic Testing” is submitted to ASE'24. This page offers access to MR-Adopt and experimental data. Additionally, it provides supplementary materials that are omitted from the paper due to space limitations.


**Table of Contents**
- [MR-Adopt](#MR-Adopt)
- [Experimental Data](#experimental-data)
	+ Dataset
    + RQ1: Effectiveness of MR-Adopt
	+ RQ2: Effectiveness of Input Transformations
	+ RQ3: Ablation Study on MR-Adop
    + RQ4: Usefulness of Input Transformations

- [Supplementary Materials](#supplementary-materials)
	+ Prompt Templates and Examples


## MR-Adopt
---
While a recent study reveals that many developer-written test cases can encode a reusable Metamorphic Relation (MR), over 70% of them directly hard-code the source input and follow-up input in the encoded relation. Such encoded MRs, which do not contain an explicit input transformation to transform the source inputs to corresponding follow-up inputs, cannot be reused with new source inputs to enhance test adequacy.

In this paper, we propose MR-Adopt (Automatic Deduction Of inPut Transformation) to automatically deduce the input transformation from the hard-coded source and follow-up inputs, aiming to enable the encoded MRs to be reused with new source inputs. With typically only one pair of source and follow-up inputs available in an MR-encoded test case as the example, we leveraged LLMs to understand the intention of the test case and generate additional examples of source-followup input pairs. This helps to guide the generation of input transformations generalizable to multiple source inputs. Besides, to mitigate the issue that LLMs generate erroneous code, we refine LLM-generated transformations by removing MR-irrelevant code elements with data-flow analysis. Finally, we assess candidate transformations based on encoded output relations and select the best transformation as the result. Evaluation results show that MR-Adopt can generate input transformations applicable to all experimental source inputs for 72.00% of encoded MRs, which is 33.33% more than using vanilla GPT-3.5. By incorporating MR-Adopt-generated input transformations, encoded MR-based test cases can effectively enhance the test adequacy, increasing the line coverage and mutation score by 10.62% and 18.91%, respectively.

The source code, executable package and tutorial of MR-Adopt can be found [here](https://github.com/MR-Adopt/MR-Adopt.github.io). 



## Experimental Data
---

Coming soon~

<!-- **MTC Dataset.** 
MR-Adopt discovered a total of 11,350 MTCs from across OSS projects. Identified MTCs can be found [here](https://github.com/MR-Adopt/MR-Adopt.github.io/blob/main/experimentalData/MTC_Dataset.json). (NOTE: The experimental projects were collected on April 5th, 2022. Due to the continuous evolution of these projects, provided signatures and paths of MTCs may be outdated. If you encounter any outdated cases, please report the issue to us. Your contributions are greatly appreciated! 😄) -->


<!-- **RQ1: Soundness.** 
To evaluate the soundness of MR-Adopt in discovering MTCs, we manually examined 164 samples, and found 97% of them are true positives. This indicates the high precision of MR-Adopt in discovering MTCs and the high quality of our MTC dataset

The true positives can be found [here](https://github.com/MR-Adopt/MR-Adopt.github.io/blob/main/experimentalData/RQ1-soundnessTPs.java). \
The false positives can be found [here](https://github.com/MR-Adopt/MR-Adopt.github.io/blob/main/experimentalData/RQ1-soundnessFPs.java). 



**RQ2: Quality.** 
MR-Adopt synthesizes codified MRs from MTCs and applies filtering to remove low-quality MRs. To evaluate the effectiveness of this process, we prepared a set of new test inputs for each codified MR. Experimental results show that 97.18% of MR-Adopt synthesized MRs are of high quality and applicability to new inputs for automated test case generation, demonstrating the practical applicability of MR-Adopt.

The detailed experimental data can be found [here](https://github.com/MR-Adopt/MR-Adopt.github.io/blob/main/experimentalData/RQ2-quality.xlsx). 

**RQ3: Usefulness.** 
To demonstrate the usefulness of synthesized MRs in enhancing test adequacy, we compared test suites constructed from MR-Adopt codified MRs against developer-written and EvoSuite-generated test suites. We employ four metrics: line coverage, mutation score, percentage of covered mutants, and test strength.

We successfully ran PIT to generate 2,170 mutants for 51 target classes from 75 reusable codified MRs (totally 4,701 lines of code in target classes).

The detailed experimental data can be found [here](https://github.com/MR-Adopt/MR-Adopt.github.io/blob/main/experimentalData/RQ3-usefulnessData.xlsx). 


**RQ4: Comprehensibility.** 
To evaluate the comprehensibility of codified MRs, we conducted a qualitative study involving three participants and 52 samples. Results show that 55.76% to 75.00% of codified MRs are easily comprehended, showcasing their potential for practical adoption by developers.

The detailed studied codified MRs can be found [here](https://github.com/MR-Adopt/MR-Adopt.github.io/blob/main/experimentalData/RQ4-comprehensibility/qualitativeStudy-codifiedMRs/).  -->


## Supplementary Materials
---
<!-- These materials are omitted from the submitted paper due to space limitations, and the PDF document can be found. -->

**Prompt Templates and Examples.** 

\tool leveraged LLMs to generate addtional input pairs and input transformations. The prompt template and concrete examples can be found [here](https://github.com/MR-Adopt/MR-Adopt.github.io/blob/main/prompts/).
