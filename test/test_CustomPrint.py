#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

def run_test(expect, function, init_cmd = '', pass_quiet=False, pass_debug=False, quiet=None,debug=None):
    import subprocess

    app = 'import os,sys; sys.path.insert(1, os.path.join(sys.path[0], "..")); import CustomPrint; '
    app += init_cmd + 'CustomPrint.' + function

    executable = ['script', '-q', '/dev/null',
                  'python', '-c', app]
    out, err = subprocess.Popen(executable, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()

    return_value = False
    got_output = (len(out) > 0) or (len(err) > 0)
    if got_output == expect:
        print("%s => %s" % ('\033[1;32mPass\033[0m', function))
        return_value = True
    else:
        print("%s => %s - expected %s got % s" % ('\033[1;31mFail\033[0m', function, str(expect), str(got_output)))
        print(app)
        print('Out:' + str(out))
        print('Err:' + str(err))

    return return_value

def run_test_group(init=False, pass_quiet=False, pass_debug=False, quiet=None, debug=None):
    init_cmd = ''
    print_info_expect=True
    print_debug_expect=False

    if init:
        if pass_quiet:
            if pass_debug:
                print("Running Tests using call to 'custom_print_init(quiet=" + str(quiet) + ", debug=" + str(debug) + ")'")
                init_cmd += 'CustomPrint.custom_print_init(quiet=' + str(quiet) + ', debug=' + str(debug) + '); '
                if quiet is None:
                    print_info_expect=True
                else:
                    print_info_expect=(not quiet)
                if debug is None:
                    print_debug_expect=False
                else:
                    print_debug_expect=debug
            else:
                print("Running Tests using call to 'custom_print_init(quiet=" + str(quiet) + ")'")
                init_cmd += 'CustomPrint.custom_print_init(quiet=' + str(quiet) + '); '
                if quiet is None:
                    print_info_expect=True
                else:
                    print_info_expect=(not quiet)
                print_debug_expect=False
        else:
            if pass_debug:
                print("Running Tests using call to 'custom_print_init(debug=" + str(debug) + ")'")
                init_cmd += 'CustomPrint.custom_print_init(debug=' + str(debug) + '); '
                print_info_expect=True
                if debug is None:
                    print_debug_expect=False
                else:
                    print_debug_expect=debug
            else:
                print("Running Tests using empty call to 'custom_print_init()'")
                init_cmd += 'CustomPrint.custom_print_init(); '
                print_info_expect=True
                print_debug_expect=False
    else:
        print("Running Tests with no call to 'custom_print_init()'")

    success = True

    success = (run_test(expect=True,               function='print_to_console("print_to_console()")',                                              init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    success = (run_test(expect=print_info_expect,  function='print_info("print_info (no extra parameters)")',                  init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=print_info_expect,  function='print_info("print_info (parameter quiet=None)", quiet=None)',     init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=True,               function='print_info("print_info (parameter quiet=False)", quiet=False)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=False,              function='print_info("print_info (parameter quiet=True)", quiet=True)',     init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    success = (run_test(expect=print_debug_expect, function='print_debug("print_debug (no extra parameters)")',                init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=print_debug_expect, function='print_debug("print_debug (parameter debug=None)", debug=None)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=False,              function='print_debug("print_debug (parameter debug=False)", debug=False)', init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=True,               function='print_debug("print_debug (parameter debug=True)", debug=True)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    success = (run_test(expect=print_info_expect,  function='print_warning("print_warning (no extra parameters)")',            init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    success = (run_test(expect=print_info_expect,  function='print_warning("print_warning (parameter quiet=None)", quiet=None)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=True,               function='print_warning("print_warning (parameter quiet=False)", quiet=False)', init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=False,              function='print_warning("print_warning (parameter quiet=True)", quiet=True)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    success = (run_test(expect=print_info_expect,  function='print_warning("print_warning (parameter debug=None)", debug=None)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=print_info_expect,  function='print_warning("print_warning (parameter debug=False)", debug=False)', init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=print_info_expect,  function='print_warning("print_warning (parameter debug=True)", debug=True)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    success = (run_test(expect=True,               function='print_warning("print_warning (parameter debug=False)", quiet=False, debug=False)', init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=True,               function='print_warning("print_warning (parameter debug=True)", quiet=False, debug=True)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=True,               function='print_warning("print_warning (parameter debug=None)", quiet=False, debug=None)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    success = (run_test(expect=print_info_expect,  function='print_warning("print_warning (parameter quiet=None, debug=False)", quiet=None, debug=False)', init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=print_info_expect,  function='print_warning("print_warning (parameter quiet=None, debug=True)", quiet=None, debug=True)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=print_info_expect,  function='print_warning("print_warning (parameter quiet=None, debug=None)", quiet=None, debug=None)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    success = (run_test(expect=False,              function='print_warning("print_warning (parameter quiet=True, debug=False)", quiet=True, debug=False)', init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=False,              function='print_warning("print_warning (parameter quiet=True, debug=True)", quiet=True, debug=True)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=False,              function='print_warning("print_warning (parameter quiet=True, debug=None)", quiet=True, debug=None)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    success = (run_test(expect=True,               function='print_warning("print_warning (parameter quiet=False, debug=False)", quiet=False, debug=False)', init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=True,               function='print_warning("print_warning (parameter quiet=False, debug=True)", quiet=False, debug=True)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=True,               function='print_warning("print_warning (parameter quiet=False, debug=None)", quiet=False, debug=None)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    success = (run_test(expect=True,               function='print_error("print_debug (parameter debug=False)", debug=False)', init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=True,               function='print_error("print_debug (parameter debug=True)", debug=True)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=True,               function='print_error("print_debug (no extra parameters)")',                init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)
    success = (run_test(expect=True,               function='print_error("print_debug (parameter debug=None)", debug=None)',   init_cmd=init_cmd, pass_quiet=pass_quiet, pass_debug=pass_debug, quiet=quiet, debug=debug) and success)

    if not success:
        exit(1)

    return success

def tests():
    import subprocess
    rows, columns = subprocess.check_output(['stty', 'size']).decode().split()

    print('=' * int(columns))
    run_test_group(init=False)
    print('=' * int(columns))
    run_test_group(init=True)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, quiet=None)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, quiet=True)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, quiet=False)
    print('=' * int(columns))
    run_test_group(init=True, pass_debug=True, debug=None)
    print('=' * int(columns))
    run_test_group(init=True, pass_debug=True, debug=True)
    print('=' * int(columns))
    run_test_group(init=True, pass_debug=True, debug=False)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, pass_debug=True, quiet=None, debug=None)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, pass_debug=True, quiet=True, debug=None)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, pass_debug=True, quiet=False, debug=None)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, pass_debug=True, quiet=None, debug=True)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, pass_debug=True, quiet=True, debug=True)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, pass_debug=True, quiet=False, debug=True)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, pass_debug=True, quiet=None, debug=False)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, pass_debug=True, quiet=True, debug=False)
    print('=' * int(columns))
    run_test_group(init=True, pass_quiet=True, pass_debug=True, quiet=False, debug=False)
    print('=' * int(columns))


tests()
