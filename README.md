# FEAS
FEAS is an automated theorem proving (ATP) agent specifically designed for solving functional equation problems within the Lean theorem prover environment. It builds upon the foundational work of the COPRA project (https://github.com/trishullab/copra) but is tailored exclusively for Lean, focusing on specialized techniques relevant to this domain.

## Setup Instructions
The setup for FEAS follows the same procedure as the COPRA project, tailored for Lean. Below are the relevant setup steps from the COPRA README, adapted for FEAS:

1. **Create and Activate a Miniconda Environment:**
   - Set up a `Miniconda` environment and activate it.

2. **Project Setup:**
   - Navigate to the project's root directory and execute the setup script: `./src/scripts/setup.sh`.

3. **Configure Environment Variables for Lean:**
   - Add the following line to your `.bashrc` file:
     ```
     export PATH="/home/$USER/.elan/bin:$PATH"
     ```

4. **API Key Configuration:**
   - Create a file named `.secrets/openai_key.json` in the project root directory containing your OpenAI API key:
     ```json
     {
       "organization": "<your-organization-id>",
       "api_key": "<your-api-key>"
     }
     ```

   Note: The `setup.sh` script includes some configurations for Coq and Isabelle which are not needed for FEAS.

5. **FunEq dataset Lean Project Configuration:**
   - Run the following commands in `data/benchmarks/FunEq` directory:
     ```
     leanpkg configure
     leanproject get-mathlib-cache
     leanproject build
     ```

## Running FEAS Experiments
To conduct experiments using FEAS, use the script `src/main/eval_benchmark.py` with the specified parameters:
- `eval_settings=n_60_dfs_gpt4_128k always`
- Set `prompt_settings` according to the desired context:
  - `lean_few_shot` for few-shot scenarios
  - `lean_dfs` for COPRA agent configurations
  - `lean_dfs_block` for FEAS agent
  - `lean_dfs_block_strategy` for FEAS agent with heuristics

- Define the `benchmark` parameter based on the problem complexity:
  - `simple_funeq` for simple problems
  - `intermediate_funeq` for intermediate-level problems
  - `imo_a1_funeq` for IMO shortlisted A1 problems
  - `imo_funeq` for other IMO shortlisted problems
  - `funeq` for running all problems of FunEq
