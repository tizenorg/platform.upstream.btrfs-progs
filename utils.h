/*
 * Copyright (C) 2007 Oracle.  All rights reserved.
 *
 * This program is free software; you can redistribute it and/or
 * modify it under the terms of the GNU General Public
 * License v2 as published by the Free Software Foundation.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * General Public License for more details.
 *
 * You should have received a copy of the GNU General Public
 * License along with this program; if not, write to the
 * Free Software Foundation, Inc., 59 Temple Place - Suite 330,
 * Boston, MA 021110-1307, USA.
 */

#ifndef __UTILS__
#define __UTILS__
int make_btrfs(int fd, u64 new_blocks[4], u64 num_bytes, u32 nodesize,
		u32 leafsize, u32 sectorsize, u32 stripesize);
int btrfs_make_root_dir(struct btrfs_trans_handle *trans,
			struct btrfs_root *root, u64 objectid);
#endif