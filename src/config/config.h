/*************************************************************************
 * Copyright (C) 2018-2019 Blue Brain Project
 *
 * This file is part of NMODL distributed under the terms of the GNU
 * Lesser General Public License. See top-level LICENSE file for details.
 *************************************************************************/

#pragma once

/**
 * \dir
 * \brief Global project configurations
 *
 * \file
 * \brief Version information and units file path
 */

#include <fstream>
#include <string>
#include <vector>

namespace nmodl {

/**
 * \brief Project version information
 */
struct Version {
    /// git revision id
    static const std::string GIT_REVISION;

    /// project tagged version in the cmake
    static const std::string NMODL_VERSION;

    /// return version string (version + git id) as a string
    static std::string to_string() {
        return NMODL_VERSION + " " + GIT_REVISION;
    }
};

/**
 * \brief Information of units database i.e. `nrnunits.lib`
 */
struct NrnUnitsLib {
    /// paths where nrnunits.lib can be found
    static const std::vector<std::string> NRNUNITSLIB_PATH;

    /**
     * Return path of units database file
     */
    static std::string get_path() {
        for (const auto& path: NRNUNITSLIB_PATH) {
            std::ifstream f(path.c_str());
            if (f.good()) {
                return path;
            }
        }
        throw std::runtime_error("Could not found nrnunits.lib");
    }
};

}  // namespace nmodl
