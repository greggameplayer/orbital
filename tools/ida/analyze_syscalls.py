#!/usr/bin/env python

syscall_list = {
    0: "sys_nosys",
    1: "sys_exit",
    2: "sys_fork",
    3: "sys_read",
    4: "sys_write",
    5: "sys_open",
    6: "sys_close",
    7: "sys_wait4",
    8: "sys_creat",
    9: "sys_link",
    10: "sys_unlink",
    11: "sys_execv",
    12: "sys_chdir",
    13: "sys_fchdir",
    14: "sys_mkd",
    15: "sys_chmod",
    16: "sys_chown",
    17: "sys_obreak",
    18: "sys_getfsstat",
    19: "sys_lseek",
    20: "sys_getpid",
    21: "sys_mount",
    22: "sys_unmount",
    23: "sys_setuid",
    24: "sys_getuid",
    25: "sys_geteuid",
    26: "sys_ptrace",
    27: "sys_recvmsg",
    28: "sys_sendmsg",
    29: "sys_recvfrom",
    30: "sys_accept",
    31: "sys_getpeername",
    32: "sys_getsockname",
    33: "sys_access",
    34: "sys_chflags",
    35: "sys_fchflags",
    36: "sys_sync",
    37: "sys_kill",
    38: "sys_stat",
    39: "sys_getppid",
    40: "sys_lstat",
    41: "sys_dup",
    42: "sys_pipe",
    43: "sys_getegid",
    44: "sys_profil",
    45: "sys_ktrace",
    46: "sys_sigaction",
    47: "sys_getgid",
    48: "sys_sigprocmask",
    49: "sys_getlogin",
    50: "sys_setlogin",
    51: "sys_acct",
    52: "sys_sigpending",
    53: "sys_sigaltstack",
    54: "sys_ioctl",
    55: "sys_reboot",
    56: "sys_revoke",
    57: "sys_symlink",
    58: "sys_readlink",
    59: "sys_execve",
    60: "sys_umask",
    61: "sys_chroot",
    62: "sys_fstat",
    63: "sys_getkerninfo",
    64: "sys_getpagesize",
    65: "sys_msync",
    66: "sys_vfork",
    67: "sys_vread",
    68: "sys_vwrite",
    69: "sys_sbrk",
    70: "sys_sstk",
    71: "sys_mmap",
    72: "sys_ovadvise",
    73: "sys_munmap",
    74: "sys_mprotect",
    75: "sys_madvise",
    76: "sys_vhangup",
    77: "sys_vlimit",
    78: "sys_mincore",
    79: "sys_getgroups",
    80: "sys_setgroups",
    81: "sys_getpgrp",
    82: "sys_setpgid",
    83: "sys_setitimer",
    84: "sys_wait",
    85: "sys_swapon",
    86: "sys_getitimer",
    87: "sys_gethostname",
    88: "sys_sethostname",
    89: "sys_getdtablesize",
    90: "sys_dup2",
    91: "sys_getdopt",
    92: "sys_fcntl",
    93: "sys_select",
    94: "sys_setdopt",
    95: "sys_fsync",
    96: "sys_setpriority",
    97: "sys_socket",
    98: "sys_connect",
    99: "sys_netcontrol",
    100: "sys_getpriority",
    101: "sys_netabort",
    102: "sys_netgetsockinfo",
    103: "sys_sigreturn",
    104: "sys_bind",
    105: "sys_setsockopt",
    106: "sys_listen",
    107: "sys_vtimes",
    108: "sys_sigvec",
    109: "sys_sigblock",
    110: "sys_sigsetmask",
    111: "sys_sigsuspend",
    112: "sys_sigstack",
    113: "sys_socketex",
    114: "sys_socketclose",
    115: "sys_vtrace",
    116: "sys_gettimeofday",
    117: "sys_getrusage",
    118: "sys_getsockopt",
    119: "sys_resuba",
    120: "sys_readv",
    121: "sys_writev",
    122: "sys_settimeofday",
    123: "sys_fchown",
    124: "sys_fchmod",
    125: "sys_netgetiflist",
    126: "sys_setreuid",
    127: "sys_setregid",
    128: "sys_rename",
    129: "sys_truncate",
    130: "sys_ftruncate",
    131: "sys_flock",
    132: "sys_mkfifo",
    133: "sys_sendto",
    134: "sys_shutdown",
    135: "sys_socketpair",
    136: "sys_mkdir",
    137: "sys_rmdir",
    138: "sys_utimes",
    139: "sys_sigreturn",
    140: "sys_adjtime",
    141: "sys_kqueueex",
    142: "sys_gethostid",
    143: "sys_sethostid",
    144: "sys_getrlimit",
    145: "sys_setrlimit",
    146: "sys_killpg",
    147: "sys_setsid",
    148: "sys_quotactl",
    149: "sys_quota",
    150: "sys_getsockname",
    151: "sys_sem_lock",
    152: "sys_sem_wakeup",
    153: "sys_asyncdaemon",
    154: "sys_nlm_syscall",
    155: "sys_nfssvc",
    156: "sys_getdirentries",
    157: "sys_statfs",
    158: "sys_fstatfs",
    160: "sys_lgetfh",
    161: "sys_getfh",
    162: "sys_getdomainname",
    163: "sys_setdomainname",
    164: "sys_uname",
    165: "sys_sysarch",
    166: "sys_rtprio",
    169: "sys_semsys",
    170: "sys_msgsys",
    171: "sys_shmsys",
    173: "sys_pread",
    174: "sys_pwrite",
    175: "sys_setfib",
    176: "sys_ntp_adjtime",
    177: "sys_sfork",
    178: "sys_getdescriptor",
    179: "sys_setdescriptor",
    181: "sys_setgid",
    182: "sys_setegid",
    183: "sys_seteuid",
    184: "sys_lfs_bmapv",
    185: "sys_lfs_markv",
    186: "sys_lfs_segclean",
    187: "sys_lfs_segwait",
    188: "sys_stat",
    189: "sys_fstat",
    190: "sys_lstat",
    191: "sys_pathconf",
    192: "sys_fpathconf",
    194: "sys_getrlimit",
    195: "sys_setrlimit",
    196: "sys_getdirentries",
    197: "sys_mmap",
    198: "sys_nosys",
    199: "sys_lseek",
    200: "sys_truncate",
    201: "sys_ftruncate",
    202: "sys_sysctl",
    203: "sys_mlock",
    204: "sys_munlock",
    205: "sys_undelete",
    206: "sys_futimes",
    207: "sys_getpgid",
    208: "sys_newreboot",
    209: "sys_poll",
    220: "sys_semctl",
    221: "sys_semget",
    222: "sys_semop",
    223: "sys_semconfig",
    224: "sys_msgctl",
    225: "sys_msgget",
    226: "sys_msgsnd",
    227: "sys_msgrcv",
    228: "sys_shmat",
    229: "sys_shmctl",
    230: "sys_shmdt",
    231: "sys_shmget",
    232: "sys_clock_gettime",
    233: "sys_clock_settime",
    234: "sys_clock_getres",
    235: "sys_ktimer_create",
    236: "sys_ktimer_delete",
    237: "sys_ktimer_settime",
    238: "sys_ktimer_gettime",
    239: "sys_ktimer_getoverrun",
    240: "sys_nasleep",
    241: "sys_ffclock_getcounter",
    242: "sys_ffclock_setestimate",
    243: "sys_ffclock_getestimate",
    247: "sys_clock_getcpuclockid2",
    248: "sys_ntp_gettime",
    250: "sys_minherit",
    251: "sys_rfork",
    252: "sys_openbsd_poll",
    253: "sys_issetugid",
    254: "sys_lchown",
    255: "sys_aio_read",
    256: "sys_aio_write",
    257: "sys_lio_listio",
    272: "sys_getdents",
    274: "sys_lchmod",
    275: "sys_lchown",
    276: "sys_lutimes",
    277: "sys_msync",
    278: "sys_nstat",
    279: "sys_nfstat",
    280: "sys_nlstat",
    289: "sys_preadv",
    290: "sys_pwritev",
    297: "sys_fhstatfs",
    298: "sys_fhopen",
    299: "sys_fhstat",
    300: "sys_modnext",
    301: "sys_modstat",
    302: "sys_modfnext",
    303: "sys_modfind",
    304: "sys_kldload",
    305: "sys_kldunload",
    306: "sys_kldfind",
    307: "sys_kldnext",
    308: "sys_kldstat",
    309: "sys_kldfirstmod",
    310: "sys_getsid",
    311: "sys_setresuid",
    312: "sys_setresgid",
    313: "sys_signasleep",
    314: "sys_aio_return",
    315: "sys_aio_suspend",
    316: "sys_aio_cancel",
    317: "sys_aio_error",
    318: "sys_aio_read",
    319: "sys_aio_write",
    320: "sys_lio_listio",
    321: "sys_yield",
    322: "sys_thr_sleep",
    323: "sys_thr_wakeup",
    324: "sys_mlockall",
    325: "sys_munlockall",
    326: "sys_getcwd",
    327: "sys_sched_setparam",
    328: "sys_sched_getparam",
    329: "sys_sched_setscheduler",
    330: "sys_sched_getscheduler",
    331: "sys_sched_yield",
    332: "sys_sched_get_priority_max",
    333: "sys_sched_get_priority_min",
    334: "sys_sched_rr_get_interval",
    335: "sys_utrace",
    336: "sys_sendfile",
    337: "sys_kldsym",
    338: "sys_jail",
    339: "sys_nnpfs_syscall",
    340: "sys_sigprocmask",
    341: "sys_sigsuspend",
    342: "sys_sigaction",
    343: "sys_sigpending",
    344: "sys_sigreturn",
    345: "sys_sigtimedwait",
    346: "sys_sigwaitinfo",
    347: "sys_acl_get_file",
    348: "sys_acl_set_file",
    349: "sys_acl_get_fd",
    350: "sys_acl_set_fd",
    351: "sys_acl_delete_file",
    352: "sys_acl_delete_fd",
    353: "sys_acl_aclcheck_file",
    354: "sys_acl_aclcheck_fd",
    355: "sys_extattrctl",
    356: "sys_extattr_set_file",
    357: "sys_extattr_get_file",
    358: "sys_extattr_delete_file",
    359: "sys_aio_waitcomplete",
    360: "sys_getresuid",
    361: "sys_getresgid",
    362: "sys_kqueue",
    363: "sys_kevent",
    364: "sys_cap_get_proc",
    365: "sys_cap_set_proc",
    366: "sys_cap_get_fd",
    367: "sys_cap_get_file",
    368: "sys_cap_set_fd",
    369: "sys_cap_set_file",
    371: "sys_extattr_set_fd",
    372: "sys_extattr_get_fd",
    373: "sys_extattr_delete_fd",
    374: "sys_setugid",
    375: "sys_nfsclnt",
    376: "sys_eaccess",
    377: "sys_afs3_syscall",
    378: "sys_nmount",
    379: "sys_mtypeprotect",
    380: "sys_kse_wakeup",
    381: "sys_kse_create",
    382: "sys_kse_thr_interrupt",
    383: "sys_kse_release",
    384: "sys_mac_get_proc",
    385: "sys_mac_set_proc",
    386: "sys_mac_get_fd",
    387: "sys_mac_get_file",
    388: "sys_mac_set_fd",
    389: "sys_mac_set_file",
    390: "sys_kenv",
    391: "sys_lchflags",
    392: "sys_uuidgen",
    393: "sys_sendfile",
    394: "sys_mac_syscall",
    395: "sys_getfsstat",
    396: "sys_statfs",
    397: "sys_fstatfs",
    398: "sys_fhstatfs",
    400: "sys_ksem_close",
    401: "sys_ksem_post",
    402: "sys_ksem_wait",
    403: "sys_ksem_trywait",
    404: "sys_ksem_init",
    405: "sys_ksem_open",
    406: "sys_ksem_unlink",
    407: "sys_ksem_getvalue",
    408: "sys_ksem_destroy",
    409: "sys_mac_get_pid",
    410: "sys_mac_get_link",
    411: "sys_mac_set_link",
    412: "sys_extattr_set_link",
    413: "sys_extattr_get_link",
    414: "sys_extattr_delete_link",
    415: "sys_mac_execve",
    416: "sys_sigaction",
    417: "sys_sigreturn",
    418: "sys_xstat",
    419: "sys_xfstat",
    420: "sys_xlstat",
    421: "sys_getcontext",
    422: "sys_setcontext",
    423: "sys_swapcontext",
    424: "sys_swapoff",
    425: "sys_acl_get_link",
    426: "sys_acl_set_link",
    427: "sys_acl_delete_link",
    428: "sys_acl_aclcheck_link",
    429: "sys_sigwait",
    430: "sys_thr_create",
    431: "sys_thr_exit",
    432: "sys_thr_self",
    433: "sys_thr_kill",
    436: "sys_jail_attach",
    437: "sys_extattr_list_fd",
    438: "sys_extattr_list_file",
    439: "sys_extattr_list_link",
    440: "sys_kse_switchin",
    441: "sys_ksem_timedwait",
    442: "sys_thr_suspend",
    443: "sys_thr_wake",
    444: "sys_kldunloadf",
    445: "sys_audit",
    446: "sys_auditon",
    447: "sys_getauid",
    448: "sys_setauid",
    449: "sys_getaudit",
    450: "sys_setaudit",
    451: "sys_getaudit_addr",
    452: "sys_setaudit_addr",
    453: "sys_auditctl",
    454: "sys_umtx_op",
    455: "sys_thr_new",
    456: "sys_sigqueue",
    457: "sys_kmq_open",
    458: "sys_kmq_setattr",
    459: "sys_kmq_timedreceive",
    460: "sys_kmq_timedsend",
    461: "sys_kmq_tify",
    462: "sys_kmq_unlink",
    463: "sys_abort2",
    464: "sys_thr_set_name",
    465: "sys_aio_fsync",
    466: "sys_rtprio_thread",
    469: "sys_getpath_fromfd",
    470: "sys_getpath_fromaddr",
    471: "sys_sctp_peeloff",
    472: "sys_sctp_generic_sendmsg",
    473: "sys_sctp_generic_sendmsg_iov",
    474: "sys_sctp_generic_recvmsg",
    475: "sys_pread",
    476: "sys_pwrite",
    477: "sys_mmap",
    478: "sys_lseek",
    479: "sys_truncate",
    480: "sys_ftruncate",
    481: "sys_thr_kill2",
    482: "sys_shm_open",
    483: "sys_shm_unlink",
    484: "sys_cpuset",
    485: "sys_cpuset_setid",
    486: "sys_cpuset_getid",
    487: "sys_cpuset_getaffinity",
    488: "sys_cpuset_setaffinity",
    489: "sys_faccessat",
    490: "sys_fchmodat",
    491: "sys_fchownat",
    492: "sys_fexecve",
    493: "sys_fstatat",
    494: "sys_futimesat",
    495: "sys_linkat",
    496: "sys_mkdirat",
    497: "sys_mkfifoat",
    498: "sys_mkdat",
    499: "sys_openat",
    500: "sys_readlinkat",
    501: "sys_renameat",
    502: "sys_symlinkat",
    503: "sys_unlinkat",
    504: "sys_posix_openpt",
    505: "sys_gssd_syscall",
    506: "sys_jail_get",
    507: "sys_jail_set",
    508: "sys_jail_remove",
    509: "sys_closefrom",
    510: "sys_semctl",
    511: "sys_msgctl",
    512: "sys_shmctl",
    513: "sys_lpathconf",
    514: "sys_cap_new",
    515: "sys_cap_rights_get",
    516: "sys_cap_enter",
    517: "sys_cap_getmode",
    518: "sys_pdfork",
    519: "sys_pdkill",
    520: "sys_pdgetpid",
    521: "sys_pdwait4",
    522: "sys_pselect",
    523: "sys_getloginclass",
    524: "sys_setloginclass",
    525: "sys_rctl_get_racct",
    526: "sys_rctl_get_rules",
    527: "sys_rctl_get_limits",
    528: "sys_rctl_add_rule",
    529: "sys_rctl_remove_rule",
    530: "sys_posix_fallocate",
    531: "sys_posix_fadvise",
    532: "sys_regmgr_call",
    533: "sys_jitshm_create",
    534: "sys_jitshm_alias",
    535: "sys_dl_get_list",
    536: "sys_dl_get_info",
    537: "sys_dl_notify_event",
    538: "sys_evf_create",
    539: "sys_evf_delete",
    540: "sys_evf_open",
    541: "sys_evf_close",
    542: "sys_evf_wait",
    543: "sys_evf_trywait",
    544: "sys_evf_set",
    545: "sys_evf_clear",
    546: "sys_evf_cancel",
    547: "sys_query_memory_protection",
    548: "sys_batch_map",
    549: "sys_osem_create",
    550: "sys_osem_delete",
    551: "sys_sys_osem_open",
    552: "sys_sys_osem_close",
    553: "sys_sys_osem_wait",
    554: "sys_sys_osem_trywait",
    555: "sys_sys_osem_post",
    556: "sys_sys_osem_cancel",
    557: "sys_sys_namedobj_create",
    558: "sys_sys_namedobj_delete",
    559: "sys_sys_set_vm_container",
    560: "sys_sys_debug_init",
    561: "sys_sys_suspend_process",
    562: "sys_sys_resume_process",
    563: "sys_sys_opmc_enable",
    564: "sys_sys_opmc_disable",
    565: "sys_sys_opmc_set_ctl",
    566: "sys_sys_opmc_set_ctr",
    567: "sys_sys_opmc_get_ctr",
    568: "sys_sys_budget_create",
    569: "sys_sys_budget_delete",
    570: "sys_sys_budget_get",
    571: "sys_sys_budget_set",
    572: "sys_sys_virtual_query",
    573: "sys_sys_mdbg_call",
    574: "sys_sys_sblock_create",
    575: "sys_sys_sblock_delete",
    576: "sys_sys_sblock_enter",
    577: "sys_sys_sblock_exit",
    578: "sys_sys_sblock_xenter",
    579: "sys_sys_sblock_xexit",
    580: "sys_sys_eport_create",
    581: "sys_sys_eport_delete",
    582: "sys_sys_eport_trigger",
    583: "sys_sys_eport_open",
    584: "sys_sys_eport_close",
    585: "sys_sys_is_in_sandbox",
    586: "sys_sys_dmem_container",
    587: "sys_sys_get_authinfo",
    588: "sys_sys_mname",
    589: "sys_sys_dynlib_dlopen",
    590: "sys_sys_dynlib_dlclose",
    591: "sys_sys_dynlib_dlsym",
    592: "sys_sys_dynlib_get_list",
    593: "sys_sys_dynlib_get_info",
    594: "sys_sys_dynlib_load_prx",
    595: "sys_sys_dynlib_unload_prx",
    596: "sys_sys_dynlib_do_copy_relocations",
    597: "sys_sys_dynlib_prepare_dlclose",
    598: "sys_sys_dynlib_get_proc_param",
    599: "sys_sys_dynlib_process_needed_and_relocate",
    600: "sys_sys_sandbox_path",
    601: "sys_sys_mdbg_service",
    602: "sys_sys_randomized_path",
    603: "sys_sys_rdup",
    604: "sys_sys_dl_get_metadata",
    605: "sys_sys_workaround8849",
    606: "sys_sys_is_development_mode",
    607: "sys_sys_get_self_auth_info",
    608: "sys_sys_dynlib_get_info_ex",
    609: "sys_sys_budget_getid",
    610: "sys_sys_budget_get_ptype",
    611: "sys_sys_get_paging_stats_of_all_threads",
    612: "sys_sys_get_proc_type_info",
    613: "sys_sys_get_resident_count",
    614: "sys_sys_prepare_to_suspend_process",
    615: "sys_sys_get_resident_fmem_count",
    616: "sys_sys_thr_get_name",
    617: "sys_sys_set_gpo",
    618: "sys_get_paging_stats_of_all_objects",
    619: "sys_test_debug_rwmem",
    620: "sys_free_stack",
    621: "sys_suspend_system",
    622: "sys_ipmimgr_call",
    623: "sys_get_gpo",
    624: "sys_get_vm_map_timestamp",
    625: "sys_opmc_set_hw",
    626: "sys_opmc_get_hw",
    627: "sys_get_cpu_usage_all",
    628: "sys_mmap_dmem",
    629: "sys_physhm_open",
    630: "sys_physhm_unlink",
    631: "sys_resume_internal_hdd",
    632: "sys_thr_suspend_ucontext",
    633: "sys_thr_resume_ucontext",
    634: "sys_thr_get_ucontext",
    635: "sys_thr_set_ucontext",
    636: "sys_set_timezone_info",
    637: "sys_set_phys_fmem_limit",
    638: "sys_utc_to_localtime",
    639: "sys_localtime_to_utc",
    640: "sys_set_uevt",
    641: "sys_get_cpu_usage_proc",
    642: "sys_get_map_statistics",
    643: "sys_set_chicken_switches",
    644: "sys_extend_page_table_pool",
    646: "sys_get_kernel_mem_statistics",
    647: "sys_get_sdk_compiled_version",
    648: "sys_app_state_change",
    649: "sys_dynlib_get_obj_member",
    650: "sys_budget_get_ptype_of_budget",
    651: "sys_prepare_to_resume_process",
    652: "sys_process_terminate",
    653: "sys_blockpool_open",
    654: "sys_blockpool_map",
    655: "sys_blockpool_unmap",
    656: "sys_dynlib_get_info_for_libdbg",
    657: "sys_blockpool_batch",
    658: "sys_fdatasync",
    659: "sys_dynlib_get_list2",
    660: "sys_dynlib_get_info2",
    661: "sys_aio_submit",
    662: "sys_aio_multi_delete",
    663: "sys_aio_multi_wait",
    664: "sys_aio_multi_poll",
    665: "sys_aio_get_data",
    666: "sys_aio_multi_cancel",
    667: "sys_get_bio_usage_all",
    668: "sys_aio_create",
    669: "sys_aio_submit_cmd",
    670: "sys_aio_init",
    671: "sys_get_page_table_stats",
    672: "sys_dynlib_get_list_for_libdbg",
}
