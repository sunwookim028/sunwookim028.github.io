---
layout: homepage
---

## About Me

I am a Fulbright scholar seeking Ph.D. positions (EE or CS) starting Fall 2025. I have research experiences with GPUs and hardware-software co-design, supported by academic training across the computing stack. I aim to study **computer systems integrating heterogeneous components**, with respect to concrete applications like AI or data systems. 

I aim to advance the frontier of specialized computer architectures as computing enters a new era where general-purpose scaling alone cannot meet our needs. This shift is already evident across the computing landscape, from domain-specific accelerators in academia and industry, to the widespread adoption of GPGPUs and FPGAs in cloud infrastructure, to emerging paradigms like near-data processing and quantum systems.

While these specialized architectures offer promising paths forward for demanding workloads like large language models, their adoption faces fundamental challenges. The trade-off between domain-specific efficiency and general applicability creates both technical and practical barriers. Limited hardware utilization may not justify the investment costs, while increased software and physical design complexity can offset potential performance gains.

My research aims to bridge this gap by developing cross-stack solutions that extend the applicability of specialized architectures. I will take a hands-on, systems-oriented approach, building and evaluating practical prototypes that address real-world software stacks, workload characteristics, and operating environments. While my specific focus will evolve as I join a research group, my commitment is to creating solutions that make specialized architectures more impactful and accessible.

I see myself thriving in computer systems research, both technically and personally. While [volunteering][solar-tz] with solar power grid projects in rural communities near Mount Kilimanjaro, I learned firsthand how critical technical infrastructure underpins people's lives. Today, computing has become as fundamental to society as electricity and telecommunications. Computing innovations increasingly shape how we solve human challenges. Computer systems research allows me to combine my passion for service with my love of elegant technical solutions.

I am excited to begin this research journey. If any aspect of this work interests you, I would be happy to discuss further at my email.

{% comment %} Prior Experiences {% endcomment %}
[solar-tz]: https://github.com/sunwookim028/solar-tz "Project Page"

## Research Interests

- **Computer Architecture and Systems:** heterogeneous processing / memory / IO elements.

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

## News

- **[Sept. 2024]** I am grateful to be nominated as a Fulbright scholar and receive financial support for my doctoral studies in U.S.

{% include_relative _includes/publications.md %}
