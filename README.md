# ECICP
Energy Consumption Analysis of Instruction Cache Prefetching Methods

## Introduction

The main goal of this project is to address energy consumption challenges in modern processors, specifically concerning <u>L1 instruction (L1-I) prefetching techniques</u>. Emerging server workloads often involve large instruction working sets, leading to frequent L1-I cache misses. To solve this issue, L1-I prefetchers were proposed. Previous studies on L1-I prefetching have primarily concentrated on enhancing performance while minimizing on-chip area overhead. However, the energy consumption of prefetchers has not been a primary objective in earlier work.

In this context, our work explores methods to <u>decrease the energy consumption</u>overhead attributed to using L1-I prefetchers. We identify that a significant portion of this consumption is due to the implicit pressure of the L1-I prefetcher on the cache hierarchy (L1-I and L2) rather than the prefetcher's metadata. Our research assesses their energy consumption and performance by evaluating four distinct L1-I prefetchers, namely RDIP, FNL-MMA, MANA, and PIF.

## Simulation Infrastructure

To analyze the performance and energy consumption of the selected prefetchers, we use [ChampSim](https://github.com/ChampSim/ChampSim) simulator and [CACTI-7](https://dl.acm.org/doi/10.1145/3085572), respectively. For ChampSim, we used dpc3_traces as the trace files for 50 server workloads.

## Repository Structure

This repository contains code, experiments, and results from our research on mitigating energy consumption overhead in server workloads due to L1-I prefetching techniques. Feel free to explore the codebase, experiment setups, and findings to gain a deeper understanding of our proposed approaches and optimizations.

For more detailed information, refer to this repository's respective directories and our [paper](https://ieeexplore.ieee.org/abstract/document/10306038).

---

*Note: This README provides an overview of the research and findings. For comprehensive details, consult the relevant research paper(s) and associated documentation.*
[here:](https://ieeexplore.ieee.org/abstract/document/10306038)

M. Baradaran, A. Ansari, M. Sadrosadati and H. Sarbazi-Azad, "Energy Consumption Analysis of Instruction Cache Prefetching Methods," 2023 International Symposium on Computer Architecture and High Performance Computing Workshops (SBAC-PADW), Porto Alegre, Brazil, 2023, pp. 60-67, doi: 10.1109/SBAC-PADW60351.2023.00019.
