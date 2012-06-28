# defined in the production class
exec { "make":
    cwd => "/prod/build/dir",
    path => "/usr/bin:/usr/sbin:/bin"
}

#. etc. .

# defined in the test class
exec { "make":
    cwd => "/test/build/dir",
    path => "/usr/bin:/usr/sbin:/bin"
}
