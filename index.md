---
layout: homepage
---

## About Me

<div id="standardView" style="display: block;">
<p>I am a Fulbright scholar seeking Ph.D. positions (EE or CS) starting Fall 2025. My research interests lie in cross-stack efforts to leverage <strong>specialized hardware accelerators</strong>.</p>

<p>I am excited about my research journey. If any aspect of my work interests you, I would be happy to discuss further at my email.</p>
</div>
<div id="expandedView" style="display: none;">
<p>I am a Fulbright scholar seeking Ph.D. positions (EE or CS) starting Fall 2025. My research interests lie in cross-stack efforts to leverage <strong>specialized hardware accelerators</strong>.</p>

<p>I see myself thriving in computer systems research, both technically and personally. While <a href="https://github.com/sunwookim028/solar-tz">volunteering</a> with solar power grid projects in rural communities near Mount Kilimanjaro, I learned firsthand how critical technical infrastructure underpins people's lives. Today, computing has become as fundamental to society as electricity and telecommunications. Computing innovations increasingly shape how we solve human challenges. Computer systems research allows me to combine my passion for service with my love of elegant technical solutions.</p>

<p>I am excited about my research journey. If any aspect of my work interests you, I would be happy to discuss further at my email.</p>
</div>
<button id="toggleButton">Expanded</button>

<script>
  document.getElementById('toggleButton').addEventListener('click', function() {
    var standard = document.getElementById('standardView');
    var expanded = document.getElementById('expandedView');
    if (standard.style.display === 'block') {
      standard.style.display = 'none';
      expanded.style.display = 'block';
      this.textContent = 'Standard';
    } else {
      standard.style.display = 'block';
      expanded.style.display = 'none';
      this.textContent = 'Expanded';
    }
  });
</script>


## Research Interests
- **Computer Architecture and Systems:** heterogeneous processing / memory / IO elements.

I aim to advance the frontier of specialized computer architectures as computing enters a new era where general-purpose scaling alone cannot meet our needs. This shift is already evident across the computing landscape, from domain-specific accelerators in academia and industry, to the widespread adoption of GPGPUs and FPGAs in cloud infrastructure, to emerging paradigms like near-data processing and quantum systems.

While these specialized architectures offer promising paths forward for demanding workloads like large language models, their adoption faces fundamental challenges. The trade-off between domain-specific efficiency and general applicability creates both technical and practical barriers. Limited hardware utilization may not justify the investment costs, while increased software and physical design complexity can offset potential performance gains. My research aims to bridge this gap.

### Themes
- Accelerator-rich Systems
    - **accelerator integration** e.g. taming acc. cost, where to run OS
    - **extending accelerators for wider utility** e.g. for evolving/compound workloads, CXL NMP & expander form, NPUs for linear algebra or graph workloads, multi-tenancy, programmability & reconfigurability

- Easy-to-use Heterogeneous Systems
    - **unifying interfaces** e.g. het. storage engine, memory pooling, language/framework and compilers supporting multiple machines (PyTorch)
    - **EDA/dev tools, ML adoption** e.g. richer & faster FPGA iterations, HLS/DSLs, ML for arch/OS policies/circuits

- Application-first Specialized Systems 
    - **vertical co-optimization** e.g. FPGA & algorithm co-evolution, quantum comm., DNA storage engines, robotics

{% comment %} References {% endcomment %}
[quantum-comm]: https://dl.acm.org/doi/pdf/10.1145/3643832.3661388 "Minsung Kim @Rutgers"

### Prior Experiences
- Accelerating compound bioinformatics workload with commodity GPUs (CUDA). [*Project Page*][titan]
- Hardware-software co-design for CNN inference (Python, Verilog, FPGA). [*Project Page*][npu]
- Demo of analog computing Fourier series (SPICE, PCB). [*Project Page*][analog-fourier]
- Pipelined CPU with forwarding (Verilog), xv6 scheduler / memory / file system kernel coding (C), syntax-driven c compiler (Bison, C), electronic circuit labs.

{% comment %} Prior Experiences {% endcomment %}
[npu]: https://github.com/sunwookim028/npu-codesign "Project Page"
[titan]: https://github.com/sunwookim028/titan "Project Page"
[analog-fourier]: https://github.com/sunwookim028/analog-fourier "Project Page"

[subc-compiler]: https://github.com/sunwookim028/subc-compiler "Project Page"
[tsc-cpu]: https://github.com/sunwookim028/tsc-cpu "Project Page"
[xv6-riscv-SNU]: https://github.com/sunwookim028/xv6-riscv-SNU "Project Page"

## News
- **[Sept. 2024]** I am grateful to be nominated as a Fulbright scholar and receive financial support for my doctoral studies in U.S.

{% include_relative _includes/publications.md %}
