import os

# 1. Update blueprint.md
bp_path = "/home/phandinhminh/Downloads/kltn/agents-research/.agents/blueprint.md"
with open(bp_path, "r", encoding="utf-8") as f:
    bp_content = f.read()

bp_content = bp_content.replace(
    "**Status:** FULLY EVOLVED & OPERATIONAL (Reflexion Flywheel: 8 Agents + 4 Inviolable Rules + Red-Teaming Mock Defense)",
    "**Status:** FULLY EVOLVED & OPERATIONAL (Reflexion Flywheel: 8 Agents + 5 Inviolable Rules + Remediation Circuit Breaker + Red-Teaming Mock Defense)"
)

old_rules = """### 2. Inviolable Rules Corpus (`rules/`)
1. `academic-integrity.md`: Zero-hallucination citations, table-text consistency, Fourier 180° physics, and Antigravity $0 API operation.
2. `empirical-rigor-mandate.md`: Multi-patient validation ($\ge 2$ patients), multi-seed $\mu \pm \sigma$, Wilcoxon test ($p < 0.01$), mandatory ablation matrix gate, and explicit weight-sharing accounting.
3. `zero-overclaim-and-tradeoff.md`: Zero subjective hyperbole, honest PSNR vs SSIM trade-off analysis, and strict baseline grounding (CNN LEARN 28.03 dB).
4. `physics-and-hardware-profiling.md`: Inviolable Fourier 180° geometry (50% void) and standardized GPU latency profiling (batch size 1, warm-up, `torch.cuda.synchronize()`)."""

new_rules = """### 2. Inviolable Rules Corpus (`rules/`)
1. `academic-integrity.md`: Zero-hallucination citations, table-text consistency, Fourier 180° physics, and Antigravity $0 API operation.
2. `empirical-rigor-mandate.md`: Multi-patient validation ($\ge 2$ patients), multi-seed $\mu \pm \sigma$, Wilcoxon test ($p < 0.01$), mandatory ablation matrix gate, and explicit weight-sharing accounting.
3. `zero-overclaim-and-tradeoff.md`: Zero subjective hyperbole, honest PSNR vs SSIM trade-off analysis, and strict baseline grounding (CNN LEARN 28.03 dB).
4. `physics-and-hardware-profiling.md`: Inviolable Fourier 180° geometry (50% void) and standardized GPU latency profiling (batch size 1, warm-up, `torch.cuda.synchronize()`).
5. `thesis-scope-and-milestones.md`: Separation of Tier 1 Mandatory Core Deliverables (working model, ablation matrix, controlled baselines, failure modes) vs Tier 2 Extended Scope (live demo UI, paper submissions); anti-scope-sprawl enforcement."""

bp_content = bp_content.replace(old_rules, new_rules)

if "### 4. Remediation Circuit Breaker" not in bp_content:
    circuit_breaker_sec = """

---

### 4. Remediation Circuit Breaker Protocol (Anti-Ping-Pong Guard)
- Tracks `remediation_cycle` in `.agents/.factory-state.json`.
- Strict bound: `remediation_cycle <= 2`.
- If defects flagged by Reviewers A, B, or C persist after 2 revision rounds $\\to$ **`HALT_REMEDIATION`**.
- Escalate unresolved disputes directly to the human user via `ask_question`.
"""
    bp_content += circuit_breaker_sec

with open(bp_path, "w", encoding="utf-8") as f:
    f.write(bp_content)

print("Updated blueprint.md successfully!")

# 2. Update README.md
readme_path = "/home/phandinhminh/Downloads/kltn/agents-research/.agents/README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    readme_content = f.read()

old_readme_rules = """│   ├── academic-integrity.md                 # Liêm chính trích dẫn, Fourier 180° và chế độ $0 API
│   ├── empirical-rigor-mandate.md            # Bắt buộc đa bệnh nhân, Mean ± Std, Wilcoxon và Ablation Matrix
│   ├── zero-overclaim-and-tradeoff.md        # Cấm phóng đại, phân tích thẳng thắn đánh đổi PSNR vs SSIM
│   └── physics-and-hardware-profiling.md     # Đóng băng định lý Fourier 2D và chuẩn hóa đo GPU Latency"""

new_readme_rules = """│   ├── academic-integrity.md                 # Liêm chính trích dẫn, Fourier 180° và chế độ $0 API
│   ├── empirical-rigor-mandate.md            # Bắt buộc đa bệnh nhân, Mean ± Std, Wilcoxon và Ablation Matrix
│   ├── zero-overclaim-and-tradeoff.md        # Cấm phóng đại, phân tích thẳng thắn đánh đổi PSNR vs SSIM
│   ├── physics-and-hardware-profiling.md     # Đóng băng định lý Fourier 2D và chuẩn hóa đo GPU Latency
│   └── thesis-scope-and-milestones.md        # Phân định yêu cầu bắt buộc KLTN vs mở rộng (Demo UI, Paper)"""

readme_content = readme_content.replace(old_readme_rules, new_readme_rules)
readme_content = readme_content.replace("4 Bộ quy tắc liêm chính", "5 Bộ quy tắc liêm chính")

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Updated README.md successfully!")

# 3. Update workflow.md
wf_path = "/home/phandinhminh/Downloads/kltn/agents-research/.agents/skills/research/workflow.md"
with open(wf_path, "r", encoding="utf-8") as f:
    wf_content = f.read()

old_wf_phase5 = """ Phase 5: Supreme PI Gatekeeper & Absolute Veto Verdict (professor-agent)
   ├── [ANY VETO: Reviewer A, B, or C] ──► MAJOR_REVISION with Mandatory Remediation Orders
   └── [ALL CLEAR: Score >= 0.85]       ──► ACCEPT for Defense / Publication"""

new_wf_phase5 = """ Phase 5: Supreme PI Gatekeeper & Absolute Veto Verdict (professor-agent)
   ├── [ANY VETO: Reviewer A, B, or C] ──► MAJOR_REVISION (Circuit Breaker: max 2 cycles -> HALT_REMEDIATION)
   └── [ALL CLEAR: Score >= 0.85]       ──► ACCEPT for Defense / Publication"""

wf_content = wf_content.replace(old_wf_phase5, new_wf_phase5)

if "## Remediation Circuit Breaker" not in wf_content:
    wf_remediation_doc = """
---

## Remediation Circuit Breaker Protocol (Anti-Ping-Pong Guard)
- Any VETO issued by Reviewers A, B, or C increments `remediation_cycle` in `.agents/.factory-state.json`.
- **Maximum Threshold**: 2 revision cycles (`remediation_cycle <= 2`).
- If unresolved defects persist after 2 revision rounds:
  - System triggers **`HALT_REMEDIATION`**.
  - `professor-agent` immediately suspends automated looping and prompts the human researcher via `ask_question`.
"""
    wf_content += wf_remediation_doc

with open(wf_path, "w", encoding="utf-8") as f:
    f.write(wf_content)

print("Updated workflow.md successfully!")
