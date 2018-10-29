file(REMOVE_RECURSE
  "../srv_gen"
  "../srv_gen"
  "../src/uvc_camera/srv"
)

# Per-language clean rules from dependency scanning.
foreach(lang )
  include(CMakeFiles/test-future.dir/cmake_clean_${lang}.cmake OPTIONAL)
endforeach()
