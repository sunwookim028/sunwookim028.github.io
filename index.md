---
layout: homepage
---

## About Me
<div id="standardView" style="display: block;">
<p>I am a Fulbright scholar seeking Ph.D. positions (EE or CS) starting Fall 2025. I have research experiences with GPUs and hardware-software co-design, supported by academic training across the computing stack. My interests lie in cross-stack efforts to leverage <strong>specialized hardware accelerators</strong>.</p>

<p>I look forward to my Ph.D. to build, experiment and learn systems. If you are interested in any aspect, I'd be happy to discuss futher through email!</p>
</div>
<div id="expandedView" style="display: none;">
<p>I am a Fulbright scholar seeking Ph.D. positions (EE or CS) starting Fall 2025. I have research experiences with GPUs and hardware-software co-design, supported by academic training across the computing stack. My interests lie in cross-stack efforts to leverage <strong>specialized hardware accelerators</strong>.</p>

<p>I aspire to contribute research for the wider adoption of specialized architecture. Specialization is increasingly accepted in various forms (massively parallel processors, dedicated hardware, near-data processing, quantum computers, etc.). They support demanding workloads (e.g. LLMs) and continue advancing computing systems despite slow device scaling. However, they inherently trade off general utility for high performance in specific domains. My goal is to extend utility of specialized architecture, by targetting wider, real-world operating settings. I aim to build cross-stack solutions addressing real-world complexities like diverse software stacks and input scenarios.</p>

<p>I see myself happy doing computer systems research, on both technical and personal levels. <a href="https://github.com/sunwookim028/solar-tz">Volunteer working</a> on solar power grids in rural communities near Mount. Kilimanjaro, I learned firsthand that critical infrastructure underpin people's lives. Today, computers are one of the most critical infrastructure in our communities, comparable to legal or water systems. Computer systems research is where my dedication to serve others merrily marry my enthusiasm for elegant structures.</p>

<p>I look forward to my Ph.D. to build, experiment and learn systems. If you are interested in any aspect, I'd be happy to discuss futher through email!</p>
</div>
<button id="toggleButton">Expanded</button>

<script>
  document.getElementById('toggleButton').addEventListener('click', function() {
    var standard = document.getElementById('standardView');
    var expanded = document.getElementById('expandedView');
    if (standard.style.display === 'block') {
      standard.style.display = 'none';
      expanded.style.display = 'block';
      this.textContent = 'Summarize';
    } else {
      standard.style.display = 'block';
      expanded.style.display = 'none';
      this.textContent = 'Expand';
    }
  });
</script>

{% comment %} Prior Experiences {% endcomment %}
[solar-tz]: https://github.com/sunwookim028/solar-tz "Project Page"



## Research Interests
- **Computer Architecture and Systems:** heterogeneous processing / memory / IO elements.

### Themes
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
