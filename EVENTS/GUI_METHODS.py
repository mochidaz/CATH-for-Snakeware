#######################################################################################################
#
#    This file is part of CATH || PyGame_GUI Text Editor.
#
#    CATH is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    CATH is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with CATH.  If not, see <https://www.gnu.org/licenses/>.
#
#######################################################################################################

import pygame
from pygame_gui.elements.ui_image import UIImage

# Update stat info label
def status_update(self, mouse_X = 1, mouse_Y = 1):
    
    
    cur_pos   = self.CATH.pos + 1
    line_pos  = self.CATH.current_line
    chars     = len(self.CATH.lines[self.CATH.current_line - 1]) + 1
    all_lines = len(self.CATH.lines) - 1
    caps      = self.CATH.caps
    
    if caps == 0: self.caps = "OFF"
    else        : self.caps = " ON"

    x, y = pygame.mouse.get_pos()
    if self.numbers == 1:
        x   = x + self.rel_X - self.EditorX
    else: x = x + self.rel_X - self.EditorX_old
    y       = y + self.rel_Y - (self.EditorY + self.bar_width)
    
    # Get clicks at centre of character by creating an offset
    x = x - (self.CATH.text_width // 2)
    y = y + (self.CATH.text_width // 2)
    
    character_X = round(x / self.CATH.text_width)
    line_Y      = round(y / self.CATH.text_size)
    
    self.mouse_X = character_X + 1
    self.mouse_Y = line_Y
    
    if self.mouse_X > self.CATH.max_line_chars:
        self.mouse_X = self.CATH.max_line_chars
    if self.mouse_Y >= self.CATH.max_lines:
        self.mouse_Y = self.CATH.max_lines -1
    
    if self.mouse_Y > 0:
        self.status_text = ("Line: " + str(line_pos) + " / " + str(all_lines) +
                            "  ||  Pos: " + str(cur_pos) + " / " + str(chars) +
                            "  ||  CAPS: " +  str(caps) + "  ||  MOUSE: " + str(self.mouse_X + self.CATH.new_pos)
                            + " : " + str(self.mouse_Y + self.CATH.real))        
    try:
        self.line_length = len(self.CATH.lines[self.mouse_Y + self.CATH.real - 1])
    except: Exception
    else:
        self.line_length = 0
    self.stats.set_text(self.status_text[:self.stat_label_chars])
    
    # If mouse is in writeable area allow text input
    if (self.mouse_X < self.CATH.max_line_chars and
        self.mouse_Y < self.CATH.total_lines and
        self.V_scr_grabbed == 0 and
        self.H_scr_grabbed == 0):
        
        self.CATH.no_entry = 0
    
# Text background updater
def update_bg(self, size, ui_manager):
    
    size = self.get_container().get_size()
    # Create background asset
    self.surface_element = UIImage(pygame.Rect((0, 0), size),
                                            pygame.Surface(size).convert(),
                                            manager=ui_manager,
                                            container=self,
                                            parent_element=self)
    
    self.background = pygame.Surface(size)  # make a background surface
    self.background = self.background.convert()
    if   self.theme_counter == 1: BG = (255, 255, 255)
    elif self.theme_counter == 2: BG = (0, 0, 0)
    else: BG = ui_manager.ui_theme.get_colour('dark_bg') # Fix default BG colouring...
    self.background.fill(BG)
    
