export PATH=$PATH:$HOME/.local/bin

        if [ "${WORKSPACE_PIP_CONF_BOUND}" = "true" ] ; then
          export PIP_CONFIG_FILE="${WORKSPACE_PIP_CONF_PATH}/${PARAM_PIP_CONF_FILE}"
        fi

        if [ -e "$(params.SOURCE_PATH)"/"$(params.REQUIREMENTS_FILE)" ];
        then
          pip install -r "$(params.SOURCE_PATH)"/"$(params.REQUIREMENTS_FILE)"
          pip show pytest || {
            printf "###\nWarning: Pytest is missing in your test requirements file\n###";
            pip install pytest
          }
        else
          if [ -e "$(params.REQUIREMENTS_FILE)" ];
          then
            pip install -r "$(params.REQUIREMENTS_FILE)"
          fi
          pip install pytest
        fi
        if [ -z "$(params.ARGS)" ]; then
          pytest "$(params.SOURCE_PATH)"
        else
          pytest "$(params.ARGS)" "$(params.SOURCE_PATH)"
        fi
      workingDir: $(workspaces.source.path)
