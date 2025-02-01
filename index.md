---
layout: homepage
---

## About Me

I am a Fulbright scholar seeking Ph.D. positions (EE or CS) starting Fall 2025. I have research experiences with GPUs and hardware-software co-design, supported by academic training across the computing stack. I aim to study **computer systems integrating heterogeneous components**, with respect to concrete applications like AI or data systems. 

I see myself happy doing computer systems research, on both technical and personal levels. [Volunteer working][solar-tz] on solar power grids in rural communities near Mount. Kilimanjaro, I learned firsthand that critical infrastructure underpin people's lives. Today, computers are one of the most critical infrastructure in our communities, comparable to legal or water systems. Computer systems research is where my dedication to serve others merrily marry my enthusiasm for elegant structures.

I aspire to contribute research for the wider adoption of specialized architecture. Specialization is increasingly accepted in various forms (massively parallel processors, dedicated hardware, near-data processing, quantum computers, etc.). They support demanding workloads (e.g. LLMs) and continue advancing computing systems despite slow device scaling. However, they inherently trade off general utility for high performance in specific domains. My goal is to extend utility of specialized architecture, by targetting wider, real-world operating settings. I aim to build **cross-stack solutions addressing real-world complexities** like diverse software stacks and input scenarios.

I look forward to my Ph.D. as a joyful chance to build, experiment and learn - rolling up my sleeves to create working system prototypes that span multiple layers of the stack! If you are interested in working on this quest with me, please leave me a quick email. 

{% comment %} Prior Experiences {% endcomment %}
[solar-tz]: https://github.com/sunwookim028/solar-tz "Project Page"

## Research Interests

- **Computer Architecture and Systems:** heterogeneous processing / memory / IO elements.

### Prior Experiences

- Earlier in my electronics studies, I explored alternative computing mechanisms like [analog computing][analog-fourier].
- As I learned fundamentals writing RTLs for [pipelined CPU][tsc-cpu] and hacking [xv6 kernel][xv6-riscv-SNU], I realized implementing novel hardware is only a single face of the challenge. Effective abstractions (like [OS][xv6-riscv-SNU]) and programming support (like [compilers][subc-compiler]) are crucial for their employment, and overheads in real-world scenarios could negate the hardware gains.
- To this end, I did research projects on co-optimizing multiple layers to best utilize speclized hardware for popular workloads. I designed [NPU][npu-codesign] hardware and software for ML inference, and algorithm and hardware-aware software optimization to [GPU-accelerate][titan] a compound Bioinformatics workload.

{% comment %} Prior Experiences {% endcomment %}
[analog-fourier]: https://github.com/sunwookim028/analog-fourier "Project Page"
[subc-compiler]: https://github.com/sunwookim028/subc-compiler "Project Page"
[tsc-cpu]: https://github.com/sunwookim028/tsc-cpu "Project Page"
[npu-codesign]: https://github.com/sunwookim028/npu-codesign "Project Page"
[titan]: https://github.com/sunwookim028/titan "Project Page"
[xv6-riscv-SNU]: https://github.com/sunwookim028/xv6-riscv-SNU "Project Page"

### Potential Thrusts
- Accelerator-rich Systems
    - **accelerator integration** e.g. taming acc. cost, where to run OS
    - **extending accelerators for wider utility** e.g. for evolving/compound workloads, CXL NMP & expander form, NPUs for linear algebra or graph workloads, virtualization, programmability & reconfigurability

- Easy-to-use Heterogeneous Systems
    - **unifying interfaces** e.g. het. storage engine, memory pooling, language/framework and compilers supporting multiple machines (PyTorch)
    - **EDA/dev tools, ML adoption** e.g. richer & faster FPGA iterations, HLS/DSLs, ML for arch/OS policies/circuits

- Application-first Specialized Systems 
    - **vertical co-optimization** e.g. FPGA & algorithm co-evolution, quantum comm., DNA storage engines, robotics

{% comment %} Potential Thrusts {% endcomment %}
[quantum-comm]: https://dl.acm.org/doi/pdf/10.1145/3643832.3661388 "Minsung Kim @Rutgers"

## News

- **[Sept. 2024]** I am grateful to be nominated as a Fulbright scholar and receive financial support for my doctoral studies in U.S.

{% include_relative _includes/publications.md %}
